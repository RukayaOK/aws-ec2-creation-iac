resource "aws_instance" "instance" {
  ami           = var.instance_ami
  instance_type = var.instance_type
  key_name      = aws_key_pair.key_pair.key_name
}
