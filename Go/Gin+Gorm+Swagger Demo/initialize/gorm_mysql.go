package initialize

import (
	"fmt"
	"gorm.io/driver/mysql"
	"gorm.io/gorm"
	"server/global"
)

func GormMysql() *gorm.DB {
	path := global.G_VP.Get("mysql.path")
	port := global.G_VP.Get("mysql.port")
	config := global.G_VP.Get("mysql.config")
	username := global.G_VP.Get("mysql.username")
	password := global.G_VP.Get("mysql.password")
	dbName := global.G_VP.Get("mysql.db-name")

	global.G_LOG.Info(path.(string))
	global.G_LOG.Info(port.(string))
	global.G_LOG.Info(config.(string))
	global.G_LOG.Info(username.(string))
	global.G_LOG.Info(dbName.(string))

	dsn := fmt.Sprintf("%s:%s@tcp(%s:%s)/%s?%s", username, password, path, port, dbName, config)
	db, _ := gorm.Open(mysql.Open(dsn), &gorm.Config{})
	return db
}
