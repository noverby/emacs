project('emacs', 'c',
  version : '0.1',
  default_options : ['warning_level=3', 'b_asneeded=false', 'b_lundef=false'])

cc = meson.get_compiler('c')
message(host_machine.system())
#message(cc.get_linker_id())
message(cc.get_id())
#m_dep = cc.find_library('m')
#dl_dep = cc.find_library('dl')
#rt_dep = cc.find_library('rt')
#thread_dep = dependency('threads')
z_dep = dependency('zlib')

libncurses_proj = subproject('ncurses')
ncurses_dep = libncurses_proj.get_variable('libncurses_dep')

c_flags = ['-Wno-pedantic', '-Wabi', '-Wno-bad-function-cast', '-Wcast-align', '-Wduplicated-branches', '-Wformat-nonliteral', '-Wformat-overflow=2', '-Winline', '-Wmissing-field-initializers', '-Wno-pointer-sign', '-Wno-switch', '-Woverlength-strings', '-Woverride-init', '-Wno-shadow', '-Wno-stack-protector', '-Wstrict-overflow', '-Wsuggest-attribute=const', '-Wsuggest-attribute=pure', '-Wsync-nand', '-Wtype-limits', '-Wunsafe-loop-optimizations', '-Wno-unused-const-variable', '-Wno-vla', '-Wno-redundant-decls', '-Wno-missing-field-initializers', '-Wno-override-init', '-Wno-sign-compare', '-Wno-type-limits', '-Wno-unused-parameter', '-Wno-format-nonliteral', '-Wno-unused-variable', '-Wno-duplicated-branches', '-Wno-format-overflow', '-Wno-unused-function', '-Wno-implicit-function-declaration', '-Wno-deprecated-declarations', '-Wno-shift-count-negative', '-Wno-int-conversion', '-Wno-cast-align', '-Wno-unknown-warning-option', '-Wno-null-pointer-arithmetic', '-Wno-tautological-constant-out-of-range-compare', '-Wno-shift-overflow', '-Wno-implicit-int-float-conversion', '-Wno-unsequence']

inc_dirs = include_directories(['lib', 'src'])

subdir('lib')
subdir('src')
