package initialize

import (
	"github.com/gin-gonic/gin"
	v1 "server/api/v1"
	_ "server/docs"
)
import ginSwagger "github.com/swaggo/gin-swagger" // gin-swagger middleware
import swaggerFiles "github.com/swaggo/files"     // swagger embed files

func InitRouters(router *gin.Engine) {
	// 註冊V1路由
	v1.InitV1Router(router)
	// 註冊 Swagger Docs
	router.GET("/swagger/*any", ginSwagger.WrapHandler(swaggerFiles.Handler))
}
