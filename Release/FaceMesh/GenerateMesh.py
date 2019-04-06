import os
import sys

import eos
import numpy as np
import cv2

from PIL import Image

import face_alignment

from skimage import io

timestamp = sys.argv[1]

username = os.environ.get("USERNAME")
path = "C:\\Users\\{}\\AppData\\Local\\FaceMesh\\".format(username)
image = path + "Images\\" + timestamp + ".jpg"
imagePoints = path + "Images\\" + "pointsOnImage_" + timestamp + ".jpg" #GIF
ptsfile = path + "facepts_" + timestamp + ".pts"
objpath = path + "FaceMeshOutput\\FaceMesh_" + timestamp + ".obj"


font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (25,75)
fontScale              = 3
fontColor              = (0,255,0)
lineType               = 2

def imagePTS():

    fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, flip_input=False, device='cpu')

    input = io.imread(image)
    imageCV = cv2.imread(image) #GIF
    preds = fa.get_landmarks(input)
    
    myfile = open(ptsfile, 'w')
    
    myfile.write("version: 1\nn_points:  68\n{\n")

    for p in preds:
        for i in p:
            myfile.write(str(i[0]) + " " + str(i[1]) + "\n")

    myfile.write("}")
    
    myfile.close()

    cv2.putText(imageCV,'HACKSTREET BOYS!', bottomLeftCornerOfText, font, fontScale, fontColor, lineType)
    cv2.imwrite(imagePoints, imageCV) #GIF
    gImage = Image.open(image) #GIF
    gImage1 = Image.open(imagePoints) #GIF

    imageList = [gImage,gImage1] #GIF

    imageList[0].save('pointsOnFace.gif',save_all=True, append_images=imageList[1:], duration=200, loop=0) #GIF    

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
    
    landmarks = read_pts(ptsfile)
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

    eos.core.write_obj(mesh,objpath)

def main():

    imagePTS()
    morphMesh()

    print(timestamp)
 
if __name__=='__main__':
    main()
