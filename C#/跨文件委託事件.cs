//主要.cs
var sub = new Sub();
sub.DelegateCallback += new Sub.NewDelegate(DoEvent);

void DoEvent(Action task)
{
  //do something 
}


//Sub.cs
public event Delegate DelegateCallback;
public delegate void Delegate(Action task);

//調用方式
NewDelegate(actoin)
