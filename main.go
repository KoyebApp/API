// /main.go
package main

import (
	"github.com/gin-gonic/gin"
	"my-golang-api/routes" // Import the routes package
)

func main() {
	// Initialize Gin router
	router := gin.Default()

	// Setup routes
	routes.SetupRoutes(router)

	// Serve static files (like your HTML interface)
	router.Static("/public", "./public")

	// Run the server
	router.Run(":8080")
}
