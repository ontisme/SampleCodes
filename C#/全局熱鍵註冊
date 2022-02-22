/// <summary>
/// 註冊熱鍵
/// </summary>
/// <param name="hwnd">窗口句柄</param>
/// <param name="id">熱鍵ID值，辨識用</param>
/// <param name="fsModifiers">組合鍵，Alt、Shift、Ctrl和Windows鍵</param>
/// <param name="vk">熱鍵</param>
/// <returns></returns>
[DllImport("user32.dll")]
public static extern bool RegisterHotKey(IntPtr hwnd, int id, uint fsModifiers, Keys vk);

/// <summary>
/// 註銷熱鍵
/// </summary>
/// <param name="hwnd">窗口句柄</param>
/// <param name="id">註冊熱鍵時的ID值</param>
/// <returns></returns>
[DllImport("user32.dll")]
public static extern bool UnregisterHotKey(IntPtr hwnd, int id);


//調用註冊熱鍵，註冊F7，ID為0
RegisterHotKey(Handle, 1, 0, Keys.F7);

//記得於FormClosing時調用，註銷熱鍵
UnregisterHotKey(Handle, 1);

//監聽熱鍵消息，如果為熱鍵事件觸發程式
protected override void WndProc(ref Message m)
{
    const int WM_HOTKEY = 0x0312;//如果m.Msg的值為0x0312那麼表示用戶按下了熱鍵
    if (m.Msg == WM_HOTKEY)
    {
        switch (m.WParam.ToInt32())
        {
            case 1:
                MessageBox.Show("熱鍵觸發");
                break;
        }
        base.WndProc(ref m); //將系統消息傳遞自父類的WndProc
    }
}
