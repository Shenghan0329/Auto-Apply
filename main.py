from application.shixiseng.apply import apply_shixiseng

stopApply = 'n'
while stopApply != 'y' and stopApply != 'Y':
    title = input("Enter job title: ")
    city = input("Enter city: ")
    apply_shixiseng({'keyword': title, 'city': city})
    stopApply = input("Do you want to stop applying? (y/n): ")
