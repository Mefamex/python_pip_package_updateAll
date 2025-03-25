# -*- coding: utf-8 -*- 

__project_name__ = "pipInstall_requ"
__author__ = "mefamex"
__email__ = "info@mefaex.com"
__url__ = "https://mefamex.com/projects/"
__license__ = "MIT"
__copyright__ = "MIT"
__description__ = "Python ile gereksinim dosyalarını yükler. Asenkron çalışır."
__url_github__ = "https://github.com/mefamex/python_pip_package_updateAll"
__status__ = "Prototype" 
__date__ = "2025-03-24"
__date_modify__ = "2024-03-24"
__python_version__ = ">=3.8" 
__dependencies__ = {
    "sys": "Built-in",
    "os": "Built-in",
    "time": "Built-in",
    "subprocess": "Built-in",
    "asyncio": "Built-in",
    "concurrent.futures": "Built-in"
}



import sys, os, asyncio
from subprocess import Popen, PIPE
import concurrent.futures
from time import sleep

pack_all = []
pack_installed = []
pack_warned= []
allLines = []

# process = Popen(command, shell=True, stdout=PIPE, stderr=PIPE)
# os.system(f"taskkill /F /PID {process.pid} >nul 2>&1")
def installPackage(packageName, outputWrite=True):
    packIndex : str = f"{pack_all.index(packageName):03d}"
    if outputWrite: print("\n\n")
    print(f"yükleniyor: {packIndex} - {packageName}")
    try:
        if 'VIRTUAL_ENV' in os.environ: python_executable = os.path.join(os.environ['VIRTUAL_ENV'], 'Scripts', 'python.exe')
        else:  python_executable = sys.executable
        command = [ python_executable, '-m', 'pip', 'install', '--upgrade', packageName]
        process = Popen( command, stdout=PIPE, stderr=PIPE, universal_newlines=True, creationflags=0x08000000 )
        while True:
            output = process.stdout.readline()
            if output == '' and process.poll() is not None:  break
            if output and outputWrite:  print(output.strip())
        return_code = process.poll()
        if return_code != 0:
            error_output = process.stderr.read()
            print(f"Hata oluştu  {packIndex} - {packageName} (Dönüş Kodu: {return_code}): {error_output}")
            return return_code
        print(f"\n+ yüklendi: {packIndex} - {packageName}")
        pack_installed.append(packageName)
        return True
    except Exception as e:
        print(f"Hata oluştu {packIndex} - {packageName} paketini yüklerken: {str(e)}")
        pack_warned.append(packageName)
        return False



with open('./requ_necessary.txt', 'r') as file:
    for line in file: allLines.append(line.strip())
with open('./requ_necessary-2.txt', 'r') as file:
    for line in file: allLines.append(line.strip())
with open('./requ_extra.txt', 'r') as file:
    for line in file: allLines.append(line.strip())

for q in allLines:
    if q not in pack_all and q != "": 
        pack_all.append(q)
        print(f"---{q.ljust(20, '-')}")
        sleep(0.03)

print(f"\n\n\nToplam paketler : {len(pack_all)}\n\n")

sleep(0.5)


async def install_packages_async(outputWrite=False):
    if installPackage("pip",True) is not True: 
        print("\n\n\npip yüklenemedi")
        return
    sleep(1)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        loop = asyncio.get_event_loop()
        tasks = [ loop.run_in_executor(executor, installPackage, package, outputWrite) for package in pack_all ]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(install_packages_async())
    
    print(f"\n\n\nyüklenen paketler : {len(pack_installed)}")
    for q in pack_installed: print(q)
    print(f"\n\nHata alan paketler : {len(pack_warned)}")
    for q in pack_warned: print(q)
    else: print("Hata alınan paket yok")
