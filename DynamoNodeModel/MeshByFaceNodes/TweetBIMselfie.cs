using System.Diagnostics;
using System.IO;

namespace MeshByFaceNodes
{
    public class TwitterConnection
    {
        /// <summary>
        /// This node takes the output of the MeshByFace.WebcamSelfie node (a filepath to a .jpg image as a string) and uses the EOS ML framework to derive a Mesh stored in the .obj format.
        /// </summary>
        /// <param name="filepathString">String: the fully-qualified filepath to the .jpeg created by the MeshByFace.WebcamSelfie node.</param>
        /// <returns>String: the fully-qualified filepath of the generated .obj file.</returns>
        /// <search>mesh, obj, jpeg, jpg, face</search>

        public static void TweetSelfie(string filepathString)
        {
            char[] splitter = { '\r' };

            string pythonExePath = @"python.exe";
            string pyFilePath = @"C:\Users\Oliver\AppData\Local\FaceMesh\twitter.py";

            Process process = new Process();
            process.StartInfo.FileName = pythonExePath;
            process.StartInfo.RedirectStandardOutput = true;
            process.StartInfo.UseShellExecute = false;

            process.StartInfo.Arguments = string.Concat(pyFilePath, " ", @"C:\Users\Oliver\AppData\Local\FaceMesh\Images\bimselfie.jpg");
            process.Start();
            process.WaitForExit();
        }
    }
}