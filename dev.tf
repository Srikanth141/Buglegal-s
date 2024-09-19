provider "aws" {
  region = "ap-south-1"
  access_key = "AKIAXG2NINDZIAJZWQNG"
  secret_key = "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"
}

resource "aws_instance" "name" {
  ami = "ami-0522ab6e1ddcc7055"
  instance_type = "t2.medium"
  key_name = "Roman"
  vpc_security_group_ids = [ "sg-0c330b8e17f0d9fe0" ]
  tags = {
    Name = "django"
  }
  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get upgrade -y",
      "sudo apt install python3-pip -y",
      "sudo apt install python3-venv -y",
      "sudo apt install python3-virtualenv -y",
      "pip install virtualenv",
      "python3 -m venv /home/ubuntu/kumar",
      ". /home/ubuntu/kumar/bin/activate",
      "git clone https://github.com/Srikanth141/Buglegal-s.git",
      "cd Buglegal-s",
      "pip install django-mathfilters",
      "pip install notifications",
      "pip install django_user_agents",
      "pip install django-allauth",
      "pip install ckeditor",
      "pip install matplotlib",
      "sudo apt install libmysqlclient-dev -y",
      "sudo apt install pkg-config -y",
      "pip install mysqlclient",
      "pip install -r requirements.txt",
      "pip install django",
      "python3 /home/ubuntu/Buglegal-s/manage.py makemigrations",
      "python3 /home/ubuntu/Buglegal-s/manage.py migrate",
      "python3 /home/ubuntu/Buglegal-s/manage.py runserver 0.0.0.0:8000"    
    ]
    connection {
      type     = "ssh"
      user     = "ubuntu"  
      private_key = file("Roman.pem")  
      host     = self.public_ip  
    }
  }
}
