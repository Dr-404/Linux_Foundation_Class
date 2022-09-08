
# Package Management 




#### apt   = Advanced Package Tool (High-Level tools)
- Dependency resolution

#### dpkg  = debian package (Low-Level Tools)
- can't install corresponding dependencies



## Installation with `dpkg`

1. Download required package `.deb`
2. `dpkg -i package.deb`
3. Install required dependencies 




## Installation with `apt`

````sudo apt update````

ကိုယ့် Repository ကို update လုပ်ရာမှာသုံးသည်။

```sudo apt upgrade```

ကိုယ့်ကွန်ပြူတာထဲမှာရှိတဲ့ application တွေကို upgrade လုပ်ရန်သုံးသည်။

```apt list```

Repository ထဲရှိ software အားလုံးကို List လုပ်ပေးသည်။

```apt search (pkg_name)```

ကိုယ့် ရှာချင်တဲ့ Package (application) ကို repo ထဲရှိမရှိ ရှာသည့်အခါသုံးသည်

```sudo apt install (pkg_name)```
Application ကို install လုပ်ရန်သုံးသည်။

```apt remove/purge (pkg_name)```

Application ကို Remove လုပ်သည့်အခါသုံးသည်။

```apt show (pkg_name)```

Application နဲ့ဆိုင်တဲ့ Information တွေကို ကြည့်ရန်သုံးသည်.


## Installation with `snap`

#### snap = snapcraf store
- url = `https://snapcraft.io/store`

```snap install (pkgname)```

Package တစ်ခုခုကို snap မှ install လုပ်ရန်သုံးသည်

```snap find (pkgname)```

package တစ်ခုခုကို snap store တွင် ရှာရန်သုံးသည်

```snap remove (pkgname)```

Package တစ်ခုခုကို remove လုပ်ရန် uninstall လုပ်ရန်သုံးသည်

```snap list```

snap မှ Install လုပ်ထားသော application များကို list လုပ်ကြည့်ရန်သုံးသည်

```snap refresh```

snap store ကို Update လုပ်ရန်သုံးသည်
