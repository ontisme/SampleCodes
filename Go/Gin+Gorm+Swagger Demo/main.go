package main

import (
	"server/global"
	"server/initialize"
)

// @contact.name   Example
// @title Swagger Demo
// @version 1.0
// @description Swagger API.
func main() {
	global.G_VP = initialize.Viper()     // 初始化 Viper
	global.G_LOG = initialize.Zap()      // 初始化 Logrus Logger
	global.G_DB = initialize.GormMysql() // 初始化 Gorm Mysql
	initialize.Gin()                     // 啟動 Gin Http Server
}
