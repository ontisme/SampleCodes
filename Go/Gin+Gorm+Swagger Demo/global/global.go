package global

import (
	"github.com/spf13/viper"
	"go.uber.org/zap"
	"gorm.io/gorm"
)

var (
	G_DB  *gorm.DB
	G_VP  *viper.Viper
	G_LOG *zap.Logger
)
