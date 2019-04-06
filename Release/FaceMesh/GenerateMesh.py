import os

import eos
import numpy as np

from PIL import Image

import face_alignment

from skimage import io

timestamp = 

username = os.environ.get("USERNAME")
path = "C:\\Users\\{}\\AppData\\Local\\FaceMesh\\".format(username)
image = path + "Images\\" + timestamp + ".jpg"


def imagePTS():

    fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, flip_input=False, device='cpu')

    input = io.imread(image)
    preds = fa.get_landmarks(input)

    ptsfile = path + "facepts_" + timestamp + ".pts"
    
    myfile = open(ptsfile, 'w')
    
    myfile.write("version: 1\nn_points:  68\n{\n")

    for p in preds:
        for i in p:
            myfile.write(str(i[0]) + " " + str(i[1]) + "\n")

    myfile.write("}")
    
    myfile.close()

def read_pts(filename):

    lines = open(filename).read().splitlines()
    lines = lines[3:71]

    landmarks = []
    ibug_index = 1
    for l in lines:
        coords = l.split()
        landmarks.append(eos.core.Landmark(str(ibug_index), [float(coords[0]), float(coords[1])]))
        ibug_index = ibug_index + 1

    return landmarks

def morphMesh():
    
    landmarks = read_pts(path + "facepts.pts")
    with Image.open(image) as img:
        image_width = img.size[0]
        image_height = img.size[1]

    model = eos.morphablemodel.load_model(path + "Share\\sfm_shape_3448.bin")
    blendshapes = eos.morphablemodel.load_blendshapes(path + "Share\\expression_blendshapes_3448.bin")
    # Create a MorphableModel with expressions from the loaded neutral model and blendshapes:
    morphablemodel_with_expressions = eos.morphablemodel.MorphableModel(model.get_shape_model(), blendshapes,color_model=eos.morphablemodel.PcaModel(),vertex_definitions=None,texture_coordinates=model.get_texture_coordinates())
    landmark_mapper = eos.core.LandmarkMapper(path + "Share\\ibug_to_sfm.txt")
    edge_topology = eos.morphablemodel.load_edge_topology(path + "Share\\sfm_3448_edge_topology.json")
    contour_landmarks = eos.fitting.ContourLandmarks.load(path + "Share\\ibug_to_sfm.txt")
    model_contour = eos.fitting.ModelContour.load(path + "Share\\sfm_model_contours.json")

    (mesh, pose, shape_coeffs, blendshape_coeffs) = eos.fitting.fit_shape_and_pose(morphablemodel_with_expressions,
        landmarks, landmark_mapper, image_width, image_height, edge_topology, contour_landmarks, model_contour)

    p = path + "FaceMeshOutput\\FaceMesh.obj"
    eos.core.write_obj(mesh,p)




imagePTS()

morphMesh()