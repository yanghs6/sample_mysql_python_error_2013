-- Create customUser
CREATE USER "customUser"@"%.%.%.%" IDENTIFIED BY "custom_pw";

-- Grant customUser
GRANT ALL ON *.* TO "customUser"@"%.%.%.%";
