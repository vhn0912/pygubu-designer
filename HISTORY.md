History
=======

Changes for version 0.28
  
  * Added more examples
  * Fix: 'filedialog.askopenfilename' is blocked by 'preferences.dialog' (larryw3i).
  * Translations for pygubu strings in pygubu-designer (larryw3i)

Changes for version 0.27

  * Add option to center the toplevel preview window. PR #124 @jrezai
  * Fix error loading ui file. issue #123
  * Added option for i18n support in code generated. issue #120
  * Added option for select main menu for generated app. issue #103 (partially fixed)

Changes for version 0.26.1

  * Hot fix: Error when loading old UI files. issue #123
  
Changes for version 0.26

  * Fix name collisions between widget ids, variables and commands. #115
  * Fix issue with Delete key in macOS. #119
  * Fix wiki links. #118

Changes for version 0.25

  * Make more intuitive design screen labels. #87
  * Fix options of wrap property for ScrolledText. #98
  * Improve style of generated code. #84, #85, #89, #92
  * Use black as formatter for generated code.
  * Add a new context command menu to select the current item's parent. #97, @jrezai
  * Fix Toplevel preview issues. @jrezai
  * Fix issue when changing geometry manager. #77, #80, @jrezai
  * Examples updated.

Changes for version 0.24

  * Removed Python 2.7 support, Minimum Python version required is now 3.6
  * New layout editor for container widgets. Added support to configure grid with 'all' index (issue #76)

Changes for version 0.23

  * Add support to use custom ttk styles defined by the user. Thanks to @jrezai
  * This is the last version with python 2.7 support
  * Other minor bug fixes.