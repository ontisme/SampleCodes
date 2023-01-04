package system

import (
	"github.com/gin-gonic/gin"
	"server/model/common/response"
)

func InitSystemTestRouter(group *gin.RouterGroup) {
	systemTest := group.Group("/test")
	systemTest.GET("/sys_hello", SysHello)
}

// SysHello @Summary 說Hello
// @Id 1
// @Tags Test
// @version 1.0
// @produce text/plain
// @Success 200 string string 成功後返回的值
// @Router /api/v1/test/sys_hello [get]
func SysHello(ctx *gin.Context) {
	response.Ok(ctx)
}
