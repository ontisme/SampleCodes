package initialize

import (
	"github.com/spf13/viper"
)

func Viper() *viper.Viper {
	var config string
	v := viper.New()
	v.SetConfigFile(config)
	v.SetConfigName("config")
	v.SetConfigType("yaml")
	v.AddConfigPath(".")
	err := v.ReadInConfig()
	if err != nil {
		panic("讀取設定檔出現錯誤，原因為：" + err.Error())
	}
	return v
}
