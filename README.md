# gitignorepy
fetch gitignore file from Github.com

# Install

```
pip install gitignorepy
```

# Usage
```
$ gg fetch macos >> ~/.gitignore
```

```
$ gg fetch rust
# Generated by Cargo
# will have compiled files and executables
/target/

# Remove Cargo.lock from gitignore if creating an executable, leave it for libraries
# More information here http://doc.crates.io/guide.html#cargotoml-vs-cargolock
Cargo.lock

# These are backup files generated by rustfmt
**/*.rs.bk
```

```
$ gg list
- Actionscript
- Ada
- Agda
- Android
...
- WordPress
- Xcode
- XilinxISE
- Xojo
- Yeoman
- Yii
- ZendFramework
- Zephir
- macOS
Found 182 templates.
```

```
$ gg list ru
- Drupal
- Lazarus
- Ruby
- Rust
Found 4 templates.
```