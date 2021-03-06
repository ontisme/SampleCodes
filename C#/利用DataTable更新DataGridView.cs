public DataTable dt = new DataTable();

//刷新不需要Clear DataGridView，重新初始化一次綁定即可
public void InitDataTable()
{
    dt = new DataTable();
    dt.Columns.Add("Round", typeof(int));
    dt.Columns.Add("BetTime", typeof(string));
    dt.Columns.Add("BetType", typeof(Image));
    dataGridView.DataSource = dt;
}

public void AddDataRow()
{
    DataRow dr = dt.NewRow();
    dr["Round"] = 0;
    dr["BetTime"] = DateTime.Now;
    dr["BetType"] = GetBetTypeImg(betType);
    dt.Rows.Add(dr);
}

public void EditDataRow()
{
    var LastRow = dt.Rows[dt.Rows.Count - 1];
    LastRow["Round"] = 1
    LastRow["BetTime"] = DateTime.Now;
}
