package main

import (
	"encoding/csv"
	"encoding/json"
	"fmt"
	"os"
)

// Log represents a log entry with fields that can accept different types.
type Log struct {
	Timestamp        string `json:"Timestamp"`
	Event            string `json:"Event"`
	UserID           string `json:"UserID"`
	SubscriptionType string `json:"SubscriptionType"`
	Description      string `json:"Description"`
}

func main() {
	// Read the JSON log file
	logs := []Log{}
	file, err := os.Open("security_camera_logs.json")
	if err != nil {
		fmt.Println("Error opening JSON file:", err)
		return
	}
	defer file.Close()

	decoder := json.NewDecoder(file)
	err = decoder.Decode(&logs)
	if err != nil {
		fmt.Println("Error decoding JSON:", err)
		return
	}

	// Create a CSV file to store the filtered logs
	csvFile, err := os.Create("subscription_data.csv")
	if err != nil {
		fmt.Println("Error creating CSV file:", err)
		return
	}
	defer csvFile.Close()

	csvWriter := csv.NewWriter(csvFile)
	defer csvWriter.Flush()

	// Write the CSV header
	header := []string{"UserID", "Timestamp", "Event", "SubscriptionType", "Description"}
	if err := csvWriter.Write(header); err != nil {
		fmt.Println("Error writing CSV header:", err)
		return
	}

	// Filter and write the logs to the CSV file
	for _, log := range logs {
		// Filter the logs for "Network," "Subscription," "UserInteraction," and "FirmwareUpdate" events
		//if log.Event == "Subscription" || log.Event == "UserInteraction" {
		if log.Event == "Subscription" {
			record := []string{log.UserID, log.Timestamp, log.Event, log.SubscriptionType, log.Description}
			if err := csvWriter.Write(record); err != nil {
				fmt.Println("Error writing CSV record:", err)
				return
			}
		}
	}

	fmt.Println("Filtered logs have been written to filtered_logs.csv.")
}
