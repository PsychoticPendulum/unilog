# Maintainer: Lukas Mairock <lukas.mairock@gmail.com>
pkgname=unilog
pkgver=1.3.7
pkgrel=1
pkgdesc="python logging library"
arch=('x86_64')
url="https://github.com/psychoticpendulum/unilog"
license=('GPL3')
source=("$pkgname-$pkgver.tar.gz"
        "$pkgname-$pkgver.patch")
noextract=()
md5sums=('d04151c49c6e3ded546550cd81549e3c' '17073ad9257583b2431a2edc245c0f5e')

package() {	
	cd "$pkgname"
	install -Dm 755 src/ansi.py "$pkgdir/usr/bin/$pkgname"
	install -Dm 755 src/unilog.py "$pkgdir/usr/bin/$pkgname"
	install -Dm644 ./README.md "$pkgdir/usr/share/doc/$pkgname"
}
