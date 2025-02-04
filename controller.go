// /controllers/apiController.go
package controllers

import (
	"github.com/gin-gonic/gin"
	"net/http"
)

// Handler for GET requests
func GetData(c *gin.Context) {
	// You can return any data here (this is an example)
	data := gin.H{
		"message": "This is a GET response",
	}
	c.JSON(http.StatusOK, data)
}

// Handler for POST requests
func PostData(c *gin.Context) {
	// Bind the JSON request body to a struct or map
	var requestData map[string]interface{}
	if err := c.ShouldBindJSON(&requestData); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid JSON"})
		return
	}

	// Here you can process the POST data (e.g., save it, perform operations)
	c.JSON(http.StatusOK, gin.H{
		"message": "This is a POST response",
		"data":    requestData,
	})
}
