using System.Diagnostics;
using System.IO;

namespace MeshByFaceNodes
{
    public class MeshByFacePipeline
    {
        /// <summary>
        /// This node takes the output of the MeshByFace.WebcamSelfie node (a filepath to a .jpg image as a string) and uses the EOS ML framework to derive a Mesh stored in the .obj format.
        /// </summary>
        /// <param name="timestampString">String: the fully-qualified filepath to the .jpeg created by the MeshByFace.WebcamSelfie node.</param>
        /// <returns>String: the fully-qualified filepath of the generated .obj file.</returns>
        /// <search>mesh, obj, jpeg, jpg, face</search>

        public static string CreateOBJFile(string timestampString)
        {
            char[] splitter = { '\r' };

            string pythonExePath = @"python.exe";
            string pyFilePath = @"C:\Users\Oliver\AppData\Local\FaceMesh\GenerateMesh.py";

            Process process = new Process();
            process.StartInfo.FileName = pythonExePath;
            process.StartInfo.RedirectStandardOutput = true;
            process.StartInfo.UseShellExecute = false;

            process.StartInfo.Arguments = string.Concat(pyFilePath, " ", timestampString);
            process.Start();

            StreamReader sReader = process.StandardOutput;
            string returnedValues = sReader.ReadToEnd();

            process.WaitForExit();
            return returnedValues;
        }
    }
}