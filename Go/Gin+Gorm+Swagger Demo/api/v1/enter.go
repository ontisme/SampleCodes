package v1

import (
	"github.com/gin-gonic/gin"
	"server/api/v1/system"
)

func InitV1Router(router *gin.Engine) {
	group := router.Group("/api/v1")
	system.InitSystemTestRouter(group)
}
