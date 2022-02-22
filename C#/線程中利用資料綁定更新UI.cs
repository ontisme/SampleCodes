public class ClassA : INotifyPropertyChanged
{
    private readonly ISynchronizeInvoke synchronizeInvoke; //要帶這個進去
    private int id;
    public Thread a;

    public ClassA(ISynchronizeInvoke synchronizeInvoke = null)
    {
        this.synchronizeInvoke = synchronizeInvoke;
        //更新數據
        a = new Thread(() =>
        {
            for (int i = 0; i < 999; i++)
            {
                Id = i;
                Debug.WriteLine(i % 2);
                if (i % 2 == 0)
                {
                    Check = true;
                }
                else
                {
                    Check = false;
                }
                Thread.Sleep(1000);
            }
        });
    }

    public event PropertyChangedEventHandler PropertyChanged;

    public int Id
    {
        get => this.id;
        set
        {
            if (value == this.id) return;

            this.id = value;
            this.OnPropertyChanged();
        }
    }


    //主要抄這個得寫法

    protected virtual void OnPropertyChanged([CallerMemberName] string propertyName = null)
    {
        if (this.PropertyChanged == null) return;

        if (this.synchronizeInvoke != null && this.synchronizeInvoke.InvokeRequired)
        {
            this.synchronizeInvoke.BeginInvoke(this.PropertyChanged, new object[] { this, new PropertyChangedEventArgs(propertyName) });
        }
        else
        {
            this.PropertyChanged.Invoke(this, new PropertyChangedEventArgs(propertyName));
        }
    }
}


public partial class Form1 : Form
{
    ClassA _class = new ClassA(this);
    // DataBindings 寫法
    textBox1.DataBindings.Add("Text",_class,"Id",true,DataSourceUpdateMode.OnPropertyChanged);
}
