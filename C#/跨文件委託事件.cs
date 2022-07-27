//主要.cs
var sub = new Sub();
sub.NewDelegate += new Sub.NewDelegate(BetTaskProcess);

void DoEvent(Action task)
{
  //do something 
}


//Sub.cs
public event Delegate NewDelegate;
public delegate void Delegate(Action task);

//調用方式
NewDelegate(actoin)
