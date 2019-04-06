using Dynamo.Controls;
using Dynamo.Wpf;
using Dynamo.ViewModels;

namespace Dynamo_ExplicitNodes1.UI
{
    public class HelloUINodeView : INodeViewCustomization<WebcamCapture>
    {
        private DynamoViewModel _dynamoVM;
        internal NodeView _nodeview;
        private WebcamCapture _model;

        //public FilterInfoCollection LoaclWebCamsCollection;
        
        public void CustomizeView(WebcamCapture model, NodeView nodeView)
        {
            _dynamoVM = nodeView.ViewModel.DynamoViewModel;
            _nodeview = nodeView;
            _model = model;
            var control = new Image();
            nodeView.inputGrid.Children.Add(control);
        }
        public void Dispose() {}
    }
}

