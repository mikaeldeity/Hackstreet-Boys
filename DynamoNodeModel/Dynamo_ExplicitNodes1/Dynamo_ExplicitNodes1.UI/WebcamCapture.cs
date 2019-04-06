using System.Collections.Generic;
using Dynamo.Graph.Nodes;
using Newtonsoft.Json;
using ProtoCore.AST.AssociativeAST;

namespace Dynamo_ExplicitNodes1.UI
{
    [NodeName("WebcamCapture")]
    [NodeDescription("This node uses the AForge library to access your webcam device. It saves a jpeg file locally for use in the mesh generation.")]
    [NodeCategory("MeshByFace.MeshByFaceNodes")]
    [OutPortTypes("string")]
    [IsDesignScriptCompatible]

    public class WebcamCapture : NodeModel
    {
        public const string SelfieFilename = "bimselfie";

        /// <summary>
        /// Json Constructor for nodes on Dynamo 2.0 and above.
        /// </summary>
        /// <param name="inPorts"></param>
        /// <param name="outPorts"></param>
        [JsonConstructor]
        public WebcamCapture(IEnumerable<PortModel> inPorts, IEnumerable<PortModel> outPorts) : base(inPorts, outPorts)
        {
            RegisterAllPorts();
        }

        public override IEnumerable<AssociativeNode> BuildOutputAst(List<AssociativeNode> inputAstNodes)
        {
            var stringNode = AstFactory.BuildStringNode(SelfieFilename);
            var assign = AstFactory.BuildAssignment(GetAstIdentifierForOutputIndex(0), stringNode);
            return new List<AssociativeNode> { assign };
        }

        public WebcamCapture()
        {
            OutPorts.Add(new PortModel(PortType.Output, this, new PortData("FileName", "Blablabla")));
            RegisterAllPorts();
        }
    }
}
