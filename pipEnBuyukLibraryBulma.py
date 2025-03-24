
import pkg_resources
from subprocess import call

# Yüklü paketlerin listesini al
packages = [dist.project_name for dist in pkg_resources.working_set]

# Her bir paketi güncelle
for package in packages:
    call(f"pip install --upgrade {package}", shell=True)



exit(0)







import pkg_resources
import os

def get_package_size(package_name):
    """Verilen kütüphanenin boyutunu hesaplar."""
    try:
        package = pkg_resources.get_distribution(package_name)
        package_path = package.location
        total_size = 0

        # Kütüphanenin dizinindeki tüm dosyaların boyutunu hesapla
        for dirpath, dirnames, filenames in os.walk(package_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)

        return total_size
    except Exception as e:
        print(f"Hata: {e} - {package_name} için boyut hesaplanamadı.")
        return 0

def get_all_packages_size():
    """Tüm yüklü kütüphanelerin boyutunu ve gereksinimlerini hesaplar."""
    packages = pkg_resources.working_set

    for package in packages:
        package_size = get_package_size(package.project_name)
        print(f"{package.project_name}: {package_size / (1024 * 1024):.2f} MB")

        # Gereksinimleri kontrol et
        for requirement in package.requires():
            req_size = get_package_size(requirement.project_name)
            print(f"  - Gereksinim: {requirement.project_name}: {req_size / (1024 * 1024):.2f} MB")

    print("\nHesaplama tamamlandı.")

# Fonksiyonu çağır
get_all_packages_size()





















import pkg_resources
import os

def get_package_size(package_name):
    """Verilen kütüphanenin boyutunu hesaplar."""
    try:
        package = pkg_resources.get_distribution(package_name)
        package_path = package.location
        total_size = 0

        for dirpath, dirnames, filenames in os.walk(package_path):
            total_size = 0
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
            print(total_size)

        return total_size
    except Exception as e:
        print(f"Hata: {e} - {package_name} için boyut hesaplanamadı.")
        return 0

def get_all_packages_size():
    """Tüm yüklü kütüphanelerin boyutunu ve gereksinimlerini hesaplar."""
    total_size = 0
    packages = pkg_resources.working_set

    for package in packages:
        package_size = get_package_size(package.project_name)
        total_size += package_size
        print(f"{package.project_name}: {package_size / (1024 * 1024):.2f} MB")

        # Gereksinimleri kontrol et
        for requirement in package.requires():
            req_size = get_package_size(requirement.project_name)
            total_size += req_size
            print(f"  - {requirement.project_name}: {req_size / (1024 * 1024):.2f} MB")

    print(f"\nToplam Boyut: {total_size / (1024 * 1024):.2f} MB")

# Fonksiyonu çağır
get_all_packages_size()