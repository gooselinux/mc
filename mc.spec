Summary:	User-friendly text console file manager and visual shell
Name:		mc
Version:	4.7.0.2
Release:	3%{?dist}
Epoch:		1
License:	GPLv2
Group:		System Environment/Shells
# downloaded from http://www.midnight-commander.org/downloads/28
Source0:	mc-%{version}.tar.bz2
URL:		http://www.midnight-commander.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	glib2-devel e2fsprogs-devel slang-devel gpm-devel
Requires:	dev >= 3.3-3

Patch0:		mc-extensions.patch

%description
Midnight Commander is a visual shell much like a file manager, only
with many more features. It is a text mode application, but it also
includes mouse support. Midnight Commander's best features are its
ability to FTP, view tar and zip files, and to poke into RPMs for
specific files.

%prep
%setup -q
%patch0 -p1 -b .extensions

%build
export CFLAGS="-D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE $RPM_OPT_FLAGS"
%configure	--with-screen=slang \
		--enable-charset \
		--with-samba \
		--without-x \
		--with-gpm-mouse \
		--disable-rpath \
		--enable-vfs-mcfs
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR="$RPM_BUILD_ROOT"

install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install contrib/{mc.sh,mc.csh} $RPM_BUILD_ROOT%{_sysconfdir}/profile.d

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)
%doc doc/FAQ doc/COPYING doc/NEWS doc/README
%{_bindir}/mc
%{_bindir}/mcedit
%{_bindir}/mcmfmt
%{_bindir}/mcview
%{_datadir}/mc/*
%attr(4711, vcsa, root) %{_libexecdir}/mc/cons.saver
%{_libexecdir}/mc/mc*
%{_mandir}/man1/*
%lang(es) %{_mandir}/es/man1/mc.1*
%lang(hu) %{_mandir}/hu/man1/mc.1*
%lang(it) %{_mandir}/it/man1/mc.1*
%lang(pl) %{_mandir}/pl/man1/mc.1*
%lang(ru) %{_mandir}/ru/man1/mc.1*
%lang(sr) %{_mandir}/sr/man1/mc.1*
%{_sysconfdir}/profile.d/*
%config %{_sysconfdir}/mc/Syntax
%config %{_sysconfdir}/mc/mc.charsets
%config %{_sysconfdir}/mc/mc.lib
%config(noreplace) %{_sysconfdir}/mc/mc.ext
%config(noreplace) %{_sysconfdir}/mc/*edit*
%config(noreplace) %{_sysconfdir}/mc/mc.keymap*
%config(noreplace) %{_sysconfdir}/mc/mc.menu*
%config(noreplace) %{_sysconfdir}/mc/*.ini
%config(noreplace) %{_sysconfdir}/mc/extfs/*.ini
%dir %{_datadir}/mc
%dir %{_sysconfdir}/mc
%dir %{_sysconfdir}/mc/extfs
%dir %{_libexecdir}/mc

%changelog
* Thu Feb 25 2010 Denys Vlasenko <dvlasenk@redhat.com> 4.7.0.2-3
- remove mplayer from extensions file

* Thu Feb 25 2010 Denys Vlasenko <dvlasenk@redhat.com> 4.7.0.2-2
- fix source URL and two rpmlint warnings

* Thu Feb 25 2010 Denys Vlasenko <dvlasenk@redhat.com> 4.7.0.2-1
- update to 4.7.0.2

* Fri Jan 15 2010 Jindrich Novy <jnovy@redhat.com> 4.7.0.1-1
- update to 4.7.0.1

* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1:4.7.0-0.4.pre2.1
- Rebuilt for RHEL 6

* Tue Sep  1 2009 Jindrich Novy <jnovy@redhat.com> 4.7.0-0.4.pre2
- update to 4.7.0-pre2

* Fri Aug  7 2009 Jindrich Novy <jnovy@redhat.com> 4.7.0-0.3.pre1
- support shell patterns in copy dialog (#516180)
  (http://www.midnight-commander.org/ticket/414)

* Wed Aug  5 2009 Jindrich Novy <jnovy@redhat.com> 4.7.0-0.2.pre1
- update extension binding to be more Fedora-like
- update to upstream IPv6 patch

* Mon Aug  3 2009 Jindrich Novy <jnovy@redhat.com> 4.7.0-0.1.pre1
- update to 4.7.0-pre1 (fixes #513757)

* Fri Jul 31 2009 Jindrich Novy <jnovy@redhat.com> 4.6.99-0.20090731git
- update to latest GIT mc
- forwardport prompt fix and exit patch, keep IPv6 patch and drop the others

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.6.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed May 17 2009 Jindrich Novy <jnovy@redhat.com> 4.6.2-11
- update to mc-4.6.2 release
- drop .8bit-hex, .preserveattrs, .cloexec, .7zip and part of
  .utf8-look-and-feel patch, applied upstream
- sync the rest of patches, adopt upstream version of UTF8 patch
- update URL and source links
- add required BR

* Fri May 15 2009 Jindrich Novy <jnovy@redhat.com> 4.6.2-10.pre1
- fix segfault in mc editor when pressing ctrl+right (skip one word)
  in binary file (#500818)
- don't use dpkg tools for *.deb files (#495649), thanks to Dan Horak

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.6.2-9.pre1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 Jindrich Novy <jnovy@redhat.com> 4.6.2-8.pre1
- fix a couple of UTF-8 related display bugs (#464708),
  thanks to Rafał Mużyło

* Thu Oct 23 2008 Jindrich Novy <jnovy@redhat.com> 4.6.2-7.pre1
- allow switching of trailing spaces/tab highlighting with crtl-v,
  patch from Jan Engelhardt (#464738)
- update the UTF-8 patch accordingly

* Tue Sep  2 2008 Jindrich Novy <jnovy@redhat.com> 4.6.2-6.pre1
- do not change directory in panel to subshell directory
  when switched back from subshell (#460633)

* Tue Aug  5 2008 Jindrich Novy <jnovy@redhat.com> 4.6.2-5.pre1
- don't try to parse obsolete RPM tags in RPM VFS (#457912),
  thanks to Milan Broz
- use correct extension for lzma and regenerate so that it applies
  with fuzz==0

* Fri Jun 20 2008 Jindrich Novy <jnovy@redhat.com> 4.6.2-4.pre1
- fix displaying of 7zip archive contents (#452090) - gvlat@pochta.ru

* Thu Mar 27 2008 Jindrich Novy <jnovy@redhat.com> 4.6.2-3.pre1
- don't segfault when hint or help files are missing (#439025),
  thanks to Tomas Heinrich
- fix displaying of 8bit encoded files in UTF-8 (#426756),
  thanks to Andrew Zabolotny
- don't gzip man pages, leave it to brp-compress

* Fri Mar  7 2008 Jindrich Novy <jnovy@redhat.com> 4.6.2-2.pre1
- add lzma vfs support by Lasse Collin
- update extensions patch to use xdg-open

* Mon Feb 25 2008 Jindrich Novy <jnovy@redhat.com> 4.6.2-1.pre1
- update to 4.6.2-pre1
- forwardport the UTF-8 patch to 4.6.2-pre1 and convert new
  functionality to support UTF-8

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:4.6.1a-52.20070604cvs
- Autorebuild for GCC 4.3

* Tue Jan  8 2008 Jindrich Novy <jnovy@redhat.com> 4.6.1a-51
- add -fgnu89-inline to let mc compile with gcc 4.3.0+

* Wed Nov 14 2007 Jindrich Novy <jnovy@redhat.com> 4.6.1a-50
- don't preserve attributes in copy/move while the option is
  switched off (#195614)
- rebuild to fix iso9660 vfs because of missing gawk in
  buildroot(#381751, #363611)

* Thu Aug 23 2007 Jindrich Novy <jnovy@redhat.com> 4.6.1a-49
- update License
- rebuild for ppc32

* Wed Jun 20 2007 Jindrich Novy <jnovy@redhat.com> 4.6.1a-48
- fix displaying of prompt in subshell (#244025)

* Tue Jun 19 2007 Jindrich Novy <jnovy@redhat.com> 4.6.1a-47
- refresh contents of terminal when resized during time
  expensive I/O operations (#236502)

* Tue Jun 12 2007 Jindrich Novy <jnovy@redhat.com> 4.6.1a-46
- update to new upstream CVS snapshot (2007-06-04-22)
- don't print prompts multiple times when switching
  between mc and subshell

* Mon Apr 16 2007 Jindrich Novy <jnovy@redhat.com> 4.6.1a-45
- fix segmentation fault while editing non-UTF8 files (#229383)

* Mon Apr  2 2007 Jindrich Novy <jnovy@redhat.com> 4.6.1a-44
- fix unowned directories (#233880)

* Thu Feb 15 2007 Jindrich Novy <jnovy@redhat.com> 4.6.1a-43
- display free space correctly for multiple filesystems (#225153)
  (thanks to Tomas Heinrich for patch)
- fix up configs

* Fri Feb  9 2007 Jindrich Novy <jnovy@redhat.com> 4.6.1a-42
- update to new CVS snapshot

* Tue Feb  6 2007 Jindrich Novy <jnovy@redhat.com> 4.6.1a-41
- merge review spec fixes (#226133)

* Mon Jan 22 2007 Jindrich Novy <jnovy@redhat.com> 4.6.1a-40
- update to new upstream CVS snapshot
- drop upstreamed tmpcrash patch
- reenable gpm support as it is now fixed (#168076)

* Thu Jan  4 2007 Jindrich Novy <jnovy@redhat.com> 4.6.1a-39
- update to new CVS snapshot (fixes #220828)
- update bindings again

* Thu Dec 21 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-38
- rebuild because of the %%{_host} macro change (Related: #220273)

* Mon Dec  4 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-37
- update bindings
- attempt to fcntl() descriptors appropriatelly so that subshell
  doesn't leave them open while execve()ing commands (#217027)
- more general fix for #215909

* Thu Nov 27 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-36
- don't crash when temporary directory cannot be created (#217342)

* Thu Nov 16 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-35
- update to new CVS snapshot
- drop .fishfix, .rpmconf patches, applied upstream
- fix IPv6 patch (should fix #206234 and #213212)
- don't crash when directory ending with newline is listed (#215909),
  disable support for directories with '\n' in name to avoid
  further issues (remove .uglydir patch) and report chdir error

* Wed Nov  2 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-34
- fix #214255 - sh vfs disconnects with special character in filename
- drop fish-upload patch, applied upstream

* Tue Oct 31 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-33
- display also conflicts in addition to provides/obsoletes/requires
  while browsing RPM vfs

* Fri Oct 27 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-32
- update to new CVS snapshot
- fix IPv6 FISH support
- use better UTF-8 characters for scrollbars

* Tue Oct 10 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-31
- update to new CVS snapshot

* Sun Oct 01 2006 Jesse Keating <jkeating@redhat.com> 4.6.1a-30
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-29
- add experimental IPv6 support for ftpfs (#198386), thanks to
  Dan Kopecek for the patch

* Wed Sep 13 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-28.fc6
- update to new CVS snapshot (09-12-21)
- drop .assembly, .spec patches -> applied upstream

* Tue Sep  5 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-27.fc6
- display hex values correctly even for non-UTF8 locales, thanks
  to Egmont Koblinger
- fix BuildRoot

* Sat Sep  2 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-26.fc6
- correctly highlight Requires(pre,post,preun,postun) in spec

* Wed Aug 23 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-25.fc6
- highlight AMD64 registers properly when editing assembly sources

* Mon Aug 21 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-24.fc6
- fix segfault caused by improper parsing of ls output while
  deleting files via shell link (#202623)

* Tue Aug 15 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-23.fc6
- update to new mc CVS snapshot
- drop .case, .rpmobsolete patches - applied upstream
- allow exit command even on non-local filesystems (#202440)
- use %%{?dist}

* Mon Jul 17 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-22
- use less ugly UTF-8 special characters for scrollbars
- properly highlight RPM tags that differ in case while
  editing spec file

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:4.6.1a-21.1
- rebuild

* Tue Jul 11 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-21
- update to new mc snapshot (fixes #195810)
- drop .segfault patch, applied upstream
- highlight "Serial:" and "Copyright:" obsolete RPM tags so that
  everyone is aware it's obsolete

* Mon Jul 10 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-20
- correctly display free space on devices referred to by
  symlinks (#197738)

* Fri Jun 16 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-19
- fix segfault in wordproc.c (#194562)

* Mon Jun 12 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-18
- apply 00-74, 00-78 patches from Egmont Koblinger with
  UTF-8 fixes related to filename truncation and file search

* Wed Jun  7 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-17
- apply UTF-8 fixes from Vladimir Nadvornik
- move the free space widget to the bottom of the main panel
  and don't use highlighting

* Mon May 29 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-16
- fix the free space widget patch: stat()s filesystem less
  frequently, display correct info in all circumstances

* Wed May 17 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-15
- update from CVS
- drop .fish-upload patch, applied upstream
- sync .showfree patch

* Fri Apr 28 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-14
- don't reread panel contents while in panelized mode (#188438)

* Thu Mar 30 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-13
- comment fallback to use only dd in FISH upload patch
- drop .promptfix patch so that prompt is displayed only
  once while in panels

* Tue Mar 28 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-12
- apply more robust version of FISH upload patch,
  thanks to Dmitry Butskoy (#186456)

* Thu Mar 16 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-11
- display the Layout dialog correctly on console (#185189)

* Wed Mar  8 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-10
- fix typo in extensions patch so that C sources are
  highlighted correctly (#184228)

* Tue Feb 28 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-9
- fix hotkey conflict in Layout options (#183282)
- move syntax configuration file from /usr/share/mc to /etc/mc
- save layout settings pernamently for showing free space, not
  only for current session (#182127)
- fix audio bindings, make firefox default html binding

* Sat Feb 25 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-8
- make mc FHS compliant: store config files in /etc/mc and
  extfs/*.ini files in /etc/mc/extfs instead of /usr/share/mc
  (#2188) - the oldest open Red Hat bug is now gone ;)
- fix warnings

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:4.6.1a-7.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:4.6.1a-7.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Feb  1 2006 Jindrich Novy <jnovy@redhat.com> 4.6.1a-7
- update from CVS - fixes syntax file for PHP
- make displaying of free space configurable
- fix permission highlighting (#177100)
- redirect stdout and stderr of several apps run on background
  to /dev/null to not to mess up mc interface (#178833)
- refresh directories to avoid errors caused by copying
  files to non-existent directories (#177111)
- add an option to insert changelog entry in mcedit,
  thanks to Radek Vokal

* Wed Dec 28 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-6
- display free space on a device assigned to current directory in
  main panels
- correctly diplay characters in mcview for non-UTF-8 LANG set (#174007)
  thanks to Dmitry Butskoy
    
* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Tue Dec  6 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-5
- correctly concatenate directory and file in concat_dir_and_file()
- highlight PHP files correctly (#174802)
- use evince instead of gv to view ps files
- align mini status bar with main panels

* Fri Dec  1 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-4
- don't segfault when LANG is not set, thanks to Andy Shevchenko (#174070)
- drop specsyntax patch, applied upstream
- sync NVRE with Fedoras
- depend on external slang [now updated to 2.0.5] (#174662)

* Wed Nov 16 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.23
- update from CVS to fix the usage of glibc private symbols
- don't try to display UTF8ized characters in hex viewing mode
  and display the characters correctly (#173309)

* Mon Nov 14 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.22
- update from upstream CVS for the new slang support
- use internal slang-2.0.5 in mc for now
- temporarily drop slang-devel dependency
- don't use gpm to avoid hangs caused by it (#168076, #172921),
  console mouse support works even without gpm
- display scrollbars correctly even if UTF-8 locale isn't set (#173014)
- add slang2 support to utf8 patch (Leonard den Ottolander)
- update %%description

* Mon Nov  5 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.21
- add vertical scrollbars to main panels and listboxes
- fix memleak in menu.c caused by UTF-8 patch
- display UTF-8 characters corectly in mcview (#172571)
- fix extensions patch

* Tue Oct 25 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.20
- don't display UTF-8 characters as questionmarks in xterm title (#170971)

* Mon Oct 16 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.19
- update from CVS
- convert spec to UTF-8
- sync utf8, promptfix, 64bit patches
- drop upstreamed gcc4, ftpcrash, find, symcrash, cstrans, searchfix patches
- drop ctrl-t patch
- update userhost patch to let the edited/viewed file name be displayed in
  xterm title

* Tue Oct  4 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.18
- fix off-by-one highlighting when searching backwards in mcedit (#169823)
- fix yet another duplicates in menus for Czech locale

* Mon Oct  3 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.17
- fix duplicated keyboard shortcuts in menus for Czech locale (#169734)
- fix ctrl-t page code recoding for Russian locale, thanks to
  Andy Shevchenko (#163594)

* Thu Sep 29 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.16
- fix memory leak in mc-utf8 patch, thanks to Marcin Garski (#169549)
- fix mc-find patch to support UTF-8, thanks to Victor Abramoff (#169531)
- remove bogus condition from mc-symcrash patch

* Tue Sep 13 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.15
- fix segfault when copying symlinks of a particular type and
  fix creation of dangled symlinks (#168184)

* Mon Sep  5 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.14
- backport the new Find dialog from upstream (#167493)
- disable Xorg usage and drop the dependency
- enable samba vfs
- highlight "%%check" in spec files (Mike A. Harris)

* Mon Aug 29 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.13
- don't hang when ftpfs connection times out - Hans de Goede (#166976)
- fix extension file to better fit FC (xpdf->evince, lynx->links)

* Mon Jul 25 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.12
- new mc release 4.6.1
- sync extensions patch
- fix several gcc4 signedness warnings

* Fri Jul 08 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.11
- update to mc-4.6.1-pre5
- sync .utf8, .userhost patch
- drop upstreamed .fixes patch

* Wed Jun 06 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.10
- update from CVS
- sync with .utf8 patch and some minor gcc4 fixups
- add .fixes patch
- drop upstreamed .spaceprompt patch
- update .userhost, .64bit patch
- add mcview

* Thu May 04 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.9
- update from CVS
- sync with .utf8 patch
- fix broken charset conversion feature in the .utf8 patch, 
  Andrew V. Samoilov (#154516)

* Mon Apr 04 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.8
- fix truncation to lower 32bits in statfs (src/mountlist.c)

* Thu Mar 24 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.7
- update from CVS
- sync with .utf8 patch
- add displaying of username/hostname in xterm title

* Mon Mar 21 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.6
- fix refusal to chdir/start file action when spaces are typed in
  command prompt and Enter is pressed (#151637)
- undefinition of umode_t for ppc64 is no more needed

* Thu Mar  3 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.5
- update from CVS
- sync the .utf8 patch with upstream
- fix infinite loop hang when copying/deleting some strangely
  named files (#150569)
- drop BuildRequires to gettext, XFree86-devel -> xorg-x11-devel
- don't define umode_t on ppc64

* Wed Feb  9 2005 Jindrich Novy <jnovy@redhat.com>
- don't use acs_map with not UTF8-ized slang (#147559)

* Mon Feb  7 2005 Jindrich Novy <jnovy@redhat.com>
- warning fix in .utf8 patch, missing inclusion of wchar.h in
  view.c (#147168)

* Wed Feb  2 2005 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.4
- update from CVS (fixes #143586)
- merge all UTF-8 related patches to single .utf8 patch
- drop BuildRequires gettext-devel, autopoint no more needed

* Tue Dec 21 2004 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.3
- rewrote mbstrlen() in utf8 patch, this fixes:
  - dir name truncation in command prompt for ja_JP, ko_KR locales (#142706)
  - localized texts will fit dialog windows and pull-down menus - tweak create_menu()
  - dialog titles are centered correctly
- fix bad displaying of mc logo in help (#143415)
- merge msglen patch with utf8 patch

* Wed Dec 15 2004 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.2
- update from CVS - problem in uzip.in fixed by upstream (#141844)
- fix msglen patch to deal with wide UTF-8 characters (#141875)

* Wed Dec  9 2004 Jindrich Novy <jnovy@redhat.com> 4.6.1a-0.1
- update from CVS
- sync UTF-8 patches with upstream
- drop upstreamed badsize, growbuf patches
- faster FISH upload support (#140750) - from Dmitry Butskoj

* Mon Dec  6 2004 Jindrich Novy <jnovy@redhat.com>
- add msglen patch to calculate message length correctly in UTF-8 (#141875)
  (thanks to Nickolay V. Shmyrev)
- convert hints for ru, uk, zh, man page conversion fix

* Wed Dec  1 2004 Jindrich Novy <jnovy@redhat.com> 4.6.1-0.11
- update from CVS
  - fix #141095 - extraction of symlinks from tarfs is now fine
- add growbuf patch from Roland Illig #141422 to view files
  in /proc and /sys properly

* Fri Nov 24 2004 Jindrich Novy <jnovy@redhat.com> 4.6.1-0.10
- update from CVS
- update promptfix patch, drop upstreamed strippwd patch
- add badsize patch to fix displaying of filesizes >2GB
- sync UTF-8 patches with upstream
- replace autogen.sh style with configure

* Fri Nov 12 2004 Jindrich Novy <jnovy@redhat.com>
- convert man pages to UTF-8 (#138871)

* Thu Nov  8 2004 Jindrich Novy <jnovy@redhat.com> 4.6.1-0.9
- update from CVS
- convert help files in /doc to UTF-8
- add --enable-charset (#76486)
- drop upstreamed 8bitdefault, extfs patch
- update partially upstreamed strippwd and extension patches
- add UTF-8 help patch from Vladimir Nadvornik (#136826)
- add promptfix patch

* Wed Nov  3 2004 Jindrich Novy <jnovy@redhat.com>
- drop upstreamed smallpatches patch
- install non-en man pages and fix encoding (#137036)
- fix possible mem leak in strippwd patch

* Fri Oct 22 2004 Jindrich Novy <jnovy@redhat.com>
- drop second part of the uglydir patch to display panel title
  correctly in UTF8 (#136129)

* Wed Oct 20 2004 Jindrich Novy <jnovy@redhat.com> 4.6.1-0.8
- update from CVS
- drop mc-php.syntax, more recent version in upstream
- add utf8-input patch
- sync strippwd, uglydir, extensions patches with upstream
- add 8bitdefault patch to enable 8-bit input by default

* Fri Oct 15 2004 Jindrich Novy <jnovy@redhat.com> 4.6.1-0.7
- update from CVS
- sync strippwd patch with upstream
- merged hp48.in patch to extfs patch (from Leonard den Ottolander)
- rebuilt

* Thu Oct 08 2004 Jindrich Novy <jnovy@redhat.com> 4.6.1-0.6
- update from CVS
- drop upstreamed vcsa and xtermaliases patches
- sync the rest of the patches with upstream
- update strippwd patch to eliminate passwords from dir hotlist
  and chdir error messages
- update perl scripts (Leonard den Ottolander, #127973, CAN-2004-0494)

* Wed Sep 22 2004 Jindrich Novy <jnovy@redhat.com> 4.6.1-0.5
- fixed password elimination when no '/' is present in URL

* Tue Sep 21 2004 Jindrich Novy <jnovy@redhat.com> 4.6.1-0.4
- fixed .strippwd patch to deal better with ':' and '@' in URL

* Thu Sep 17 2004 Jindrich Novy <jnovy@redhat.com> 4.6.1-0.3
- patch to prevent displaying passwords in ftp paths (#131088)
  - also removes pswd from Delete/Copy/Error dialogs, etc.
- added patch to fix/add extensions in mc.ext.in (#124242)

* Thu Sep 17 2004 Karel Zak <zakkr@zf.jcu.cz>
- patch to prevent hangs on directory with '\n' in name, (#127164)
- UTF8 hints support
- original hint files conversion to UTF8 in the spec file

* Mon Sep  6 2004 Jakub Jelinek <jakub@redhat.com> 4.6.1-0.2
- update from CVS
- remove absoluterm and troff patches

* Thu Sep  2 2004 Jakub Jelinek <jakub@redhat.com> 4.6.1-0.1
- update from CVS
  - handle INFO/LICENSE and INFO/OBSOLETES in rpm vfs (#67341)
- remove mc-cvs-unzip (#85073)
- fix hotkey handling when not UTF-8 (Leonard den Ottolander, #120735)
- allow terminal aliases for keys in mc.lib and ~/mc/ini,
  add gnome, xterm-new and rxvt aliases for xterm (#128163)

* Sat Aug 21 2004 Jakub Jelinek <jakub@redhat.com> 4.6.0-18
- 3 more quoting omissions in a.in

* Sat Aug 21 2004 Jakub Jelinek <jakub@redhat.com> 4.6.0-17
- fix shell quoting in extfs perl scripts
  (Leonard den Ottolander, #127973, CAN-2004-0494)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Apr 16 2004 Jakub Jelinek <jakub@redhat.com> 4.6.0-15
- don't use mmap if st_size doesn't fit into size_t
- fix one missed match_normal -> match_regex

* Fri Apr 16 2004 Jakub Jelinek <jakub@redhat.com> 4.6.0-14
- avoid buffer overflows in mcedit Replace function

* Wed Apr 14 2004 Jakub Jelinek <jakub@redhat.com> 4.6.0-13
- perl scripting fix

* Wed Apr 14 2004 Jakub Jelinek <jakub@redhat.com> 4.6.0-12
- fix a bug in complete.c introduced by last patch
- export MC_TMPDIR env variable
- avoid integer overflows in free diskspace % counting
- put temporary files into $MC_TMPDIR tree if possible,
  use mktemp/mkdtemp

* Mon Apr  5 2004 Jakub Jelinek <jakub@redhat.com> 4.6.0-11
- fix a bunch of buffer overflows and memory leaks (CAN-2004-0226)
- fix hardlink handling in cpio filesystem
- fix handling of filenames with single/double quotes and backslashes
  in %%{_datadir}/mc/extfs/rpm
- update php.syntax file (#112645)
- fix crash with large syntax file (#112644)
- update CAN-2003-1023 fix to still make vfs symlinks relative,
  but with bounds checking

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Jan 17 2004 Warren Togami <wtogami@redhat.com> 4.6.0-9
- rebuild

* Sat Jan 17 2004 Warren Togami <wtogami@redhat.com> 4.6.0-7
- BuildRequires glib2-devel, slang-devel, XFree86-devel,
  e2fsprogs-devel, gettext
- Copyright -> License
- PreReq -> Requires
- Explicit zero epoch in versioned dev dep
- /usr/share/mc directory ownership
- Improve summary
- (Seth Vidal QA) fix for CAN-2003-1023 (Security)

* Tue Oct 28 2003 Jakub Jelinek <jakub@redhat.com> 4.6.0-6
- rebuilt to get correct PT_GNU_STACK setting

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Feb 24 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Sat Feb 22 2003 Jakub Jelinek <jakub@redhat.com> 4.6.0-3
- second part of UTF-8ization

* Fri Feb 21 2003 Jakub Jelinek <jakub@redhat.com> 4.6.0-2
- kill unneeded patches, update the rest for 4.6.0
- build with system slang
- first part of UTF-8ization

* Fri Feb 14 2003 Havoc Pennington <hp@redhat.com> 4.6.0-1
- 4.6.0 final
- epoch 1 to work around 4.6.0pre > 4.6.0

* Thu Feb 13 2003 Havoc Pennington <hp@redhat.com> 4.6.0pre3-3
- drop our translations, they are surely out of date
- ugh, due to spec file weirdness hadn't actually used the new pre3
  tarball. disabled patches that no longer apply.
- patch for #78506

* Thu Feb 06 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- link also on mainframe against gpm-devel

* Tue Feb  4 2003 Havoc Pennington <hp@redhat.com> 4.6.0pre3-1
- pre3

* Tue Jan 28 2003 Havoc Pennington <hp@redhat.com>
- rebuild

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Dec  6 2002 Havoc Pennington <hp@redhat.com>
- 4.6.0-pre1
- comment out the patches that don't apply, 
  if someone wants to spend time fixing them 
  that'd be great

* Mon Dec 02 2002 Elliot Lee <sopwith@redhat.com>
- Remove 'percent prep' in changelog
- Fix unpackaged files

* Fri Aug 23 2002 Karsten Hopp <karsten@redhat.de>
- fix german umlaut in menues (#68130)

* Fri Jul 19 2002 Jakub Jelinek <jakub@redhat.com> 4.5.55-11
- removed trailing backslash for %%configure, which
  caused mc to build with the buildroot prefix

* Wed Jul 17 2002 Karsten Hopp <karsten@redhat.de> 4.5.55-10
- support large files (#65159, #65160)
- own /usr/lib/mc/extfs and /usr/lib/mc/syntax
- fix NL translation (#63495)

* Thu Jul  4 2002 Jakub Jelinek <jakub@redhat.com>
- fix regex usage

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Fri Apr 12 2002 Havoc Pennington <hp@redhat.com>
- patch for trpm vfs, #62306

* Wed Apr 10 2002 Havoc Pennington <hp@redhat.com>
- don't build --with-included-slang on upstream recommendation
- add uzip method from cvs, fixes some sort of format string problem
- get fix for breaking zip files while browsing them from upstream

* Tue Apr  9 2002 Havoc Pennington <hp@redhat.com>
- remove bash-specific export from mc.sh

* Thu Mar 28 2002 Havoc Pennington <hp@redhat.com>
- cons.saver rewrite to use vcsa user from Jakub, #61149
- make cons.saver attr(4711, vcsa, root)
- require new dev package

* Thu Mar  7 2002 Havoc Pennington <hp@redhat.com>
- rebuild in new environment
- 4.5.55, with lots of patch-adapting to make it build

* Fri Jan 25 2002 Havoc Pennington <hp@redhat.com>
- rebuild in rawhide
- fix prefix/share -> datadir
- comment out gmc/mcserv subpackages, place order for asbestos suit

* Mon Aug 27 2001 Havoc Pennington <hp@redhat.com>
- Add po files from sources.redhat.com

* Sun Jul 22 2001 Havoc Pennington <hp@redhat.com>
- build requires gnome-libs-devel, #49518

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Wed Apr 25 2001 Bill Nottingham <notting@redhat.com>
- fix mc-4.5.51-desktop.patch to work on ia64

* Mon Apr  2 2001 Preston Brown <pbrown@redhat.com>
- check return code of mount for failure (ewt)

* Thu Mar 22 2001 Owen Taylor <otaylor@redhat.com>
- Fix problem where CORBA notification wasn't working since last change.

* Fri Mar 16 2001 Owen Taylor <otaylor@redhat.com>
- Rescan devices on startup

* Mon Mar 12 2001  <jrb@redhat.com>
- remove man pages from mc.ext.in so that tgz and rpm browsing work in
  non LANG=C locales

* Wed Mar  7 2001 Owen Taylor <otaylor@redhat.com>
- Add patch to recognize kudzu's fstab entries
- Fix path to memstick icon

* Fri Feb 23 2001 Trond Eivind Glomsrød <teg@redhat.com>
- use %%{_tmppath}
- langify

* Tue Feb 21 2001 Akira TAGOH <tagoh@redhat.com>
- Fixed install some desktop icons for specific language.

* Fri Feb 16 2001 Akira TAGOH <tagoh@redhat.com>
- Updated Red Hat JP desktop icons.

* Wed Feb 14 2001 Jakub Jelinek <jakub@redhat.com>
- include both sys/time.h and time.h on glibc 2.2.2
- fix Japanese patch to include locale.h.

* Tue Feb  6 2001 Trond Eivind Glomsrød <teg@redhat.com>
- i18nize initscript

* Sat Jan 27 2001 Akira TAGOH <tagoh@redhat.com>
- Added Japanese patch(language specific desktop icons).

* Fri Jan 19 2001 Akira TAGOH <tagoh@redhat.com>
- Updated Japanese translation.

* Sun Jan 14 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- do not prereq %%{_sysconfdir}/init.d
- do not require gpm for s390

* Mon Aug 21 2000 Jonathan Blandford <jrb@redhat.com>
- fixed bug 16467

* Thu Aug 17 2000 Tim Powers <timp@redhat.com>
- modified my patch (again) to free quoted

* Thu Aug 17 2000 Nalin Dahyabhai <nalin@redhat.com>
- run %%configure in the build phase, not the setup
- modify Tim's patch to always just edit one file

* Thu Aug 17 2000 Than Ngo <than@redhat.com>
- fix problems viewing the package (Bug #16378)

* Thu Aug 17 2000 Tim Powers <timp@redhat.com>
- fixed bug #16269

* Fri Aug  4 2000 Tim Waugh <twaugh@redhat.com>
- make stdout/stderr writable before forking

* Wed Aug 02 2000 Jonathan Blandford <jrb@redhat.com>
- Updated desktop entries.

* Thu Jul 20 2000 Bill Nottingham <notting@redhat.com>
- move initscript back

* Wed Jul 19 2000 Jonathan Blandford <jrb@redhat.com>
- make the togglebutton patch work correctly

* Tue Jul 18 2000 Nalin Dahyabhai <nalin@redhat.com>
- fix syntax error in mcserv.init that crept in with condrestart

* Mon Jul 17 2000 Jonathan Blandford <jrb@redhat.com>
- added a toggle button to let people turn off the "you are running
  gmc as root" warning.

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul 10 2000 Preston Brown <pbrown@redhat.com>
- move initscript, add condrestart stuff

* Mon Jul 10 2000 Florian La Roche <Florian.LaRoche@redhat.de>
- remove execute bits from config/pam files

* Mon Jul  3 2000 Jonathan Blandford
- Update to 4.5.51.  Now there is a trashcan!

* Thu Jun 15 2000 Owen Taylor <otaylor@redhat.com>
- Update to 4.5.49

* Fri Jun  2 2000 Nalin Dahyabhai <nalin@redhat.com>
- modify PAM setup to use system-auth

* Mon May 22 2000 Bill Nottingham <notting@redhat.com>
- hmmm, ia64 patches fell out.

* Fri May 19 2000 Jonathan Blandford <jrb@redhat.com>
- upgrade to new version of mc.
- removed builtincpio patch

* Tue Mar  7 2000 Jeff Johnson <jbj@redhat.com>
- rebuild for sparc baud rates > 38400.

* Wed Feb 22 2000 Preston Brown <pbrown@redhat.com>
- fix mc.sh, function was not exported

* Wed Feb 17 2000 Jakub Jelinek <jakub@redhat.com>
- builtin cpio vfs, change rpm extfs to use it -
  should speed up e.g. copyout from rpm by orders of magnitude
  patch by Jan Hudec <jhud7196@artax.karlin.mff.cuni.cz>
- fix buglet in the patch

* Mon Feb 14 2000 Preston Brown <pbrown@redhat.com>
- move redhat-logos depency to gmc (#9395)

* Fri Feb 4 2000 Jonathan Blandford <jrb@redhat.com>
- changed default rpm action to be upgrade.
- Changed locale to be in mc package, instead of gmc.

* Thu Feb 3 2000 Jonathan Blandford <jrb@redhat.com>
- use /bin/rm instead of rm so that aliases won't interfere with the
  script

* Fri Sep 25 1999 Bill Nottingham <notting@redhat.com>
- chkconfig --del in %%preun, not %%postun

* Wed Sep 22 1999 Michael Fulbright <drmike@redhat.com>
- updated to 4.5.39-pre9

* Wed Aug 04 1999 Michael K. Johnson <johnsonm@redhat.com>
- moved configure to setup
- buildrequires gpm-devel so mouse works in console

* Wed Jul 22 1999 Michael Fulbright <drmike@redhat.com>
- added ${prefix}/lib/mc/syntax to mc file list
- turned off samba support

* Wed Jul  7 1999 Jonathan Blandford <jrb@redhat.com>
- updated mc to work with mc 4.5.36.  Thanks to Brian Ryner
  <bryner@uiuc.edu> for providing the patch.

* Mon Apr 19 1999 Michael Fulbright <drmike@redhat.com>
- removed rpm menu defs - we depend on gnorpm for these
- fixed bug that caused crash if group doesnt exist for file

* Thu Apr 15 1999 Michael Fulbright <drmike@redhat.com>
- cleanup several dialogs

* Mon Apr 12 1999 Michael Fulbright <drmike@redhat.com>
- true version 4.5.30

* Fri Apr 09 1999 Michael Fulbright <drmike@redhat.com>
- version pre-4.5.30 with patch to make this link on alpha properly
  Mark as version 0.7 to denote not the official 4.5.30 release

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binaries

* Wed Mar 31 1999 Michael Fulbright <drmike@redhat.com>
- fixed errata support URL

* Tue Mar 25 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.29
- added default desktop icons for Red Hat desktop
- added redhat-logos to requirements
- added README.desktop to doc list for gmc
- added locale data

* Fri Mar 25 1999 Preston Brown <pbrown@redhat.com>
- patched so that TERM variable set to xterm produces color

* Mon Mar 22 1999 Michael Fulbright <drmike@redhat.com>
- made sure %%{_sysconfdir}/pam.d/mcserv has right permissions

* Thu Mar 18 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.27

* Tue Mar 16 1999 Michael Fulbright <drmike@redhat.com>
- fix'd icon display problem

* Sun Mar 14 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.25 AND 4.5.26

* Wed Mar 10 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.24

* Mon Feb 15 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.16
- removed mc.keys from mc file list

* Fri Feb 12 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.14
- fixed file list

* Sat Feb 06 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.11

* Wed Feb 03 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.10

* Fri Jan 22 1999 Michael Fulbright <drmike@redhat.com>
- added metadata to gmc file list

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.9

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- version 4.5.6

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- updated for GNOME freeze

* Thu Aug 20 1998 Michael Fulbright <msf@redhat.com>
- rebuilt against gnome-libs 0.27 and gtk+-1.1

* Thu Jul 09 1998 Michael Fulbright <msf@redhat.com>
- made cons.saver not setuid

* Sun Apr 19 1998 Marc Ewing <marc@redhat.com>
- removed tkmc

* Wed Apr 8 1998 Marc Ewing <marc@redhat.com>
- add %%{prefix}/lib/mc/layout to gmc

* Tue Dec 23 1997 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>
- added --without-debug to configure,
- modification in %%build and %%install and cosmetic modification in packages
  headers,
- added %%{PACKAGE_VERSION} macro to Buildroot,
- removed "rm -rf $RPM_BUILD_ROOT" from prep section
- removed Packager field.

* Thu Dec 18 1997 Michele Marziani <marziani@fe.infn.it>
- Merged spec file with that from RedHat-5.0 distribution
  (now a Hurricane-based distribution is needed)
- Added patch for RPM script (didn't always work with rpm-2.4.10)
- Corrected patch for mcserv init file (chkconfig init levels)
- Added more documentation files on termcap, terminfo, xterm

* Thu Oct 30 1997 Michael K. Johnson <johnsonm@redhat.com>

- Added dependency on portmap

* Wed Oct 29 1997 Michael K. Johnson <johnsonm@redhat.com>

- fixed spec file.
- Updated to 4.1.8

* Sun Oct 26 1997 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>

- updated to 4.1.6
- added %%attr macros in %%files,
- a few simplification in %%install,
- removed glibc patch,
- fixed installing %%{_sysconfdir}/X11/wmconfig/tkmc.

* Thu Oct 23 1997 Michael K. Johnson <johnsonm@redhat.com>

- updated to 4.1.5
- added wmconfig

* Wed Oct 15 1997 Erik Troan <ewt@redhat.com>

- chkconfig is for mcserv package, not mc one

* Tue Oct 14 1997 Erik Troan <ewt@redhat.com>

- patched init script for chkconfig
- don't turn on the service by default

* Fri Oct 10 1997 Michael K. Johnson <johnsonm@redhat.com>

- Converted to new PAM conventions.
- Updated to 4.1.3
- No longer needs glibc patch.

* Thu May 22 1997 Michele Marziani <marziani@fe.infn.it>

- added support for mc alias in %%{_sysconfdir}/profile.d/mc.csh (for csh and tcsh)
- lowered number of SysV init scripts in %%{_sysconfdir}/rc.d/rc[0,1,6].d
  (mcserv needs to be killed before inet)
- removed all references to RPM_SOURCE_DIR
- restored $RPM_OPT_FLAGS when compiling
- minor cleanup of spec file: redundant directives and comments removed

* Sun May 18 1997 Michele Marziani <marziani@fe.infn.it>

- removed all references to non-existent mc.rpmfs
- added mcedit.1 to the %%files section
- reverted to un-gzipped man pages (RedHat style)
- removed double install line for mcserv.pamd

* Tue May 13 1997 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>

- added new rpmfs script,
- removed mcfn_install from mc (adding mc() to bash enviroment is in
  %%{_sysconfdir}/profile.d/mc.sh),
- %%{_sysconfdir}/profile.d/mc.sh changed to %%config,
- removed %%{prefix}/lib/mc/bin/create_vcs,
- removed %%{prefix}/lib/mc/term.

* Wed May 9 1997 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>

- changed source url,
- fixed link mcedit to mc,

* Tue May 7 1997 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>

- new version 3.5.27,
- %%dir %%{prefix}/lib/mc/icons and icons removed from tkmc,
- added commented xmc part.

* Tue Apr 22 1997 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>

- FIX spec:
   - added URL field,
   - in mc added missing %%{prefix}/lib/mc/mc.ext, %%{prefix}/lib/mc/mc.hint,
     %%{prefix}/lib/mc/mc.hlp, %%{prefix}/lib/mc/mc.lib, %%{prefix}/lib/mc/mc.menu.

* Fri Apr 18 1997 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>

- added making packages: tkmc, mcserv (xmc not work yet),
- gziped man pages,
- added %%{_sysconfdir}/pamd.d/mcserv PAM config file.
- added instaling icons,
- added %%{_sysconfdir}/profile.d/mc.sh,
- in %%doc added NEWS README,
- removed %%{prefix}/lib/mc/FAQ,
- added mcserv.init script for mcserv (start/stop on level 86).
