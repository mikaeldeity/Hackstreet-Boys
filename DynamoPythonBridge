using System;
using System.Diagnostics;
using System.IO;
using System.Windows.Forms;


namespace DynamoPythonBridge
{
    public static class ExternalPython
    {
        //public static void ExecutePython(string[] args)
        public static string GetPythonVersion()
        {
            // full path of python interpreter
            string python = @"C:\Users\Oliver\AppData\Local\Programs\Python\Python37-32\python.exe";

            // python app to call
            string myPythonApp = "import sys" + Environment.NewLine + "print(sys.version)" + Environment.NewLine;

            // Create new process start info
            ProcessStartInfo myProcessStartInfo = new ProcessStartInfo(python)
            {   // make sure we can read the output from stdout
                UseShellExecute = false,
                RedirectStandardOutput = true,
                WindowStyle = ProcessWindowStyle.Hidden,
                CreateNoWindow = true,

                // start python app with 3 arguments 
                // 1st arguments is pointer to itself, 2nd and 3rd are actual arguments we want to send
                Arguments = myPythonApp
            };

            Process myProcess = new Process();
            // assign start information to the process
            myProcess.StartInfo = myProcessStartInfo;

            // start the process
            myProcess.Start();

            // Read the standard output of the app we called. 
            // in order to avoid deadlock we will read output first and then wait for process terminate:
            StreamReader myStreamReader = myProcess.StandardOutput;
            string myString = myStreamReader.ReadLine();

            // wait exit signal from the app we called and then close it.
            myProcess.WaitForExit();
            myProcess.Close();

            // write the output we got from python app
            return "Value received from script: " + myString;
            //Console.ReadKey();
        }

        // for multiple outputs, add following line
        //[MultiReturn(new[] { "add", "mult" })]


        /// <summary>
        /// Executes a Python file supplied via the path parameter using an alternative Python engine.
        /// Input values are passed to Python script via runtime arguments.
        /// </summary>
        /// <param name="myPythonApp">Path to python file to execute</param>
        /// <param name="arguments">Arguments to pass to Python file as input</param>
        /// <returns name="Python output">Python script's output as string. Simple "print" commands in Python are enough to output here.</param>

        public static string Execute(string myPythonApp, string[] arguments)
        {
            if (myPythonApp==string.Empty || !File.Exists(myPythonApp)) return "Please supply a valid python file.";

            // full path of python interpreter
            string python = @"C:\Program Files\Anaconda2\python.exe";

            // Create new process start info
            ProcessStartInfo myProcessStartInfo = new ProcessStartInfo(python);
            string pythonArguments = String.Join(" ", arguments);

            // make sure we can read the output from stdout
            myProcessStartInfo.UseShellExecute = false;
            myProcessStartInfo.RedirectStandardOutput = true;
            myProcessStartInfo.WindowStyle = ProcessWindowStyle.Hidden;
            myProcessStartInfo.CreateNoWindow = true;

            // start python app with 3 arguments 
            // 1st arguments is pointer to itself, 2nd and 3rd are actual arguments we want to send
            myProcessStartInfo.Arguments = myPythonApp + " " + pythonArguments;

            Process myProcess = new Process();
            // assign start information to the process
            myProcess.StartInfo = myProcessStartInfo;

            // start the process
            Console.WriteLine("Calling Python script with arguments {0} ", String.Join(",", arguments));
            myProcess.Start();

            // Read the standard output of the app we called. 
            // in order to avoid deadlock we will read output first and then wait for process terminate:
            StreamReader myStreamReader = myProcess.StandardOutput;
            string pythonOutput = myStreamReader.ReadToEnd();

            // wait exit signal from the app we called and then close it.
            myProcess.WaitForExit();
            myProcess.Close();

            // for multiple outputs :
            /*
            return new Dictionary<string, object>
                {
                    { "add", (a + b) },
                    { "mult", (a * b) }
                };
                */

            // write the output we got from python app
            return pythonOutput;
        }

        public static void DisplayModelScoreResult(string input)
        {
            MessageBox.Show(input);
        }

    }

}

