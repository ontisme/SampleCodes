// 文字分割成數字陣列
YORSTRING.Split(',').Select(Int32.Parse).ToList();

// 刪除最後一個字元
Str = Str.Substring(0, levelStr.LastIndexOf("-"));
