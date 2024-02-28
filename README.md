
# COPRs for Fedora

This repository contains a collection of `.spec` files for Fedora

## Dependencies 
 - `rpm-build`
 - 'rpmdevtools'
 - `copr-cli`

## Building a Source RPM (SRPM)

Navigate to your SPEC directory, where your SPEC file and the SOURCES directory are located. Use the following command to build the Source RPM:

```bash
rpmbuild -bs --define "_srcrpmdir <destination_for_SRPM>" <path_to_SPEC_file>
```

For example:

```bash
rpmbuild -bs --define "_srcrpmdir /var/home/dev/rpmbuild/SRPMS" /var/home/dev/rpmbuild/SPECS/marp-cli.spec
```

## Uploading to rpm-ostree
 For example:

```bash
copr-cli build mecattaf/marp-cli /var/home/dev/rpmbuild/SRPMS/marp-cli-3.4.0-1.fc38.src.rpm
```

## References:
[openSuse repo](https://github.com/bmwiedemann/openSUSE/tree/master/packages)
