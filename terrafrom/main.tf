resource "aws_dynamodb_table" "test-import-table" {
  name     = "my-imported-table"
  hash_key = "UserID"
  range_key      = "Timestamp"

  billing_mode   = "PROVISIONED"
  write_capacity = 5
  read_capacity  = 5

  attribute {
    name = "UserID"
    type = "S"
  }

  attribute {
    name = "Timestamp"
    type = "S"
  }

  import_table {
    input_format = "CSV"
    input_compression_type = "NONE"

    s3_bucket_source {
      bucket = "mybucket-877"
    }

    input_format_options {
      csv {
        delimiter = ","
        header_list = ["UserID", "Timestamp", "Event","SubscriptionType","Description"]
      }
    }
  }
}