//資料集
BindingList<AppA> oCustomers = new BindingList<AppA>();
oCustomers.Add(a);
oCustomers.Add(b);
oCustomers.Add(c);

dataGridView1.AutoGenerateColumns = false; //取消自動建立欄位
dataGridView1.DataSource = oCustomers; //綁定數據源

//綁定欄位對應數據
dataGridView1.Columns["dgvId"].DataPropertyName = "Id";  
dataGridView1.Columns["dgvCheck"].DataPropertyName = "Check";
