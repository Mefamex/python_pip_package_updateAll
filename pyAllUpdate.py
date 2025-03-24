import pkg_resources
from subprocess import call

# Yüklü paketlerin listesini al
packages = [dist.project_name for dist in pkg_resources.working_set]


with open('installed_packages.txt', 'w') as file:
    for package in packages:
        file.write(package + '\n')

print("Yüklü paketler 'installed_packages.txt' dosyasına yazıldı.")



# Her bir paketi güncelle
for package in packages:
    call(f"\n\n\n\n\n\n\n\npip install --upgrade {package}", shell=True)

