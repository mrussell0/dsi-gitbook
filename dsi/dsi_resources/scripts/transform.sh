echo "Deleting morning exercises and hw folders"
find . -name '*-hw' -exec rm -rf {} \;
find . -name '*-morning' -exec git rm -rf {} \; 
find . -name '*-reflection' -exec git rm -rf {} \;
find . -name '*-presentation' -exec git rm -rf {} \;
find . -name '*-outcomes' -exec rm -rf {} \;
