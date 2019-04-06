import face_alignment
from skimage import io

fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, flip_input=False, device='cpu')

input = io.imread("C:\\Users\\Mikael\\Documents\\GitHub\\Hackstreet-Boys\\FaceAlign\\Images\\pic.jpg")
preds = fa.get_landmarks(input)

path = "C:\\Users\\Mikael\\Documents\\GitHub\\Hackstreet-Boys\\FaceAlign\\"

ptsfile = path + "facepts.pts"
 
myfile = open(ptsfile, 'w')
 
myfile.write("version: 1\nn_points:  68\n{\n")

for p in preds:
    for i in p:
        myfile.write(str(i[0]) + " " + str(i[1]) + "\n")

myfile.write("}")

myfile.close()
