type product struct {
	Name  string `json:"name"`
	Color string `json:"color"`
	Price string `json:"price"`
	Link  string `json:"link"`
}

diff := utils.Difference(Products, products2)
	for _, str := range diff {
		fmt.Println(str.(product))
		out, _ := json.Marshal(str)
		_ = notify.SendText(AccessToken, string(out))
	}
