package initialize

import (
	"github.com/gin-gonic/gin"
	"server/global"
	"server/middleware"
	"strconv"
)

func Gin() {
	r := gin.Default()

	r.Use(middleware.Cors()) // 直接放行全部跨域请求
	InitRouters(r)           // 初始化路由
	port := global.G_VP.Get("application.gin-port").(int)
	err := r.Run(":" + strconv.Itoa(port))

	if err != nil {
		return
	}
	// listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
