//在該cs重寫這段 CreateParams

protected override CreateParams CreateParams
{
    get
    {
        if (Environment.OSVersion.Version.Major >= 6)
        {
            // Vista以上     
            CreateParams cp = base.CreateParams;
            cp.ExStyle |= 0x02000000;
            return cp;
        }
        else
        {
            return base.CreateParams;
        }
    }
}
