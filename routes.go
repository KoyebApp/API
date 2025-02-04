// /routes/apiRoutes.go
package routes

import (
	"github.com/gin-gonic/gin"
	"my-golang-api/controllers" // Import the controllers package
)

func SetupRoutes(router *gin.Engine) {
	// Define the API routes
	router.GET("/api/get", controllers.GetData)   // GET route
	router.POST("/api/post", controllers.PostData) // POST route
}
