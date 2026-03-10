provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "estacao_clima" {

  bucket = "estacao-meteorologica-ingrid-devops"

  tags = {
    Projeto = "Estacao Meteorologica"
    Curso   = "DevOps"
  }

}