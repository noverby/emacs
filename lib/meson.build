glob = run_command('globbing.py')
sources = glob.stdout().strip().split('\n')
foreach src : sources
  configure_file(input: src, output: src, copy: true)
endforeach

glob = run_command('globbing-header.py')
headers = glob.stdout().strip().split('\n')
foreach hdr : headers
  configure_file(input: hdr, output: hdr, copy: true)
endforeach

conf_data = configuration_data()
conf_data.set('HAVE_DECL___FPENDING', 1)
conf_data.set('_GL_ATTRIBUTE_CONST', true)
conf_data.set('_GL_UNUSED', true)
conf_data.set('_GL_ATTRIBUTE_PURE', true)
conf_data.set('FLEXIBLE_ARRAY_MEMBER', true)
conf_data.set('PROMOTED_MODE_T', 'mode_t')
conf_data.set('HAVE_MALLOC_H', 1)
conf_data.set('HYBRID_MALLOC', 1)
conf_data.set('HAVE_LIMITS_H', 1)
conf_data.set('HAVE_MINMAX_IN_SYS_PARAM_H', 1)
conf_data.set('__STDC_WANT_IEC_60559_BFP_EXT__', 1)
conf_data.set('HAVE_SYS_TIME_H', 1)
conf_data.set('HAVE_STDINT_H', 1)
conf_data.set('HAVE_PSELECT', 1)
#conf_data.set('HAVE_PTHREAD', 1)
conf_data.set('HAVE_ZLIB', 1)
conf_data.set('HAVE_UNISTD_H', 1)
conf_data.set('HAVE_OPENAT', 1)
conf_data.set('HAVE_DUP2', 1)
conf_data.set('HAVE_FCNTL', 1)
conf_data.set('HAVE_GETGROUPS', 1)
conf_data.set('HAVE_TIMER_SETTIME', '1')
conf_data.set('GETGROUPS_T', 'gid_t')
conf_data.set('GETTIMEOFDAY_TIMEZONE', 'struct timezone')
conf_data.set('_Noreturn', '__attribute__ ((__noreturn__))')
conf_data.set('DIRECTORY_SEP', '\'/\'')
conf_data.set('NULL_DEVICE', '"/dev/null"')
conf_data.set('HAVE_PWD_H', 1)
conf_data.set('HAVE_SYS_UTSNAME_H', 1)
conf_data.set('HAVE_CFMAKERAW', 1)
conf_data.set('HAVE_CFSETSPEED', 1)
conf_data.set('HAVE_GETRLIMIT', 1)
conf_data.set('HAVE_STRUCT_DIRENT_D_TYPE', 1)
conf_data.set('HAVE_SYS_RESOURCE_H', 1)
conf_data.set('HAVE_ENVIRON_DECL', 1)
conf_data.set('_GNU_SOURCE', 1)
conf_data.set('HAVE_SOCKETS', 1)
conf_data.set('HAVE_SYS_SOCKET_H', 1)
conf_data.set('USER_FULL_NAME', 'pw->pw_gecos')
conf_data.set('HAVE_INET_SOCKETS', 1)
conf_data.set('HAVE_NET_IF_H', 1)
conf_data.set('HAVE_SYS_UN_H', 1)
conf_data.set('HAVE_IFADDRS_H', 1)
conf_data.set('HAVE_PTY_H', 1)
conf_data.set('HAVE_INET_SOCKETS', 1)
conf_data.set('subprocesses', 1)
conf_data.set('USABLE_FIONREAD', 1)
conf_data.set('HAVE_LANGINFO_CODESET', 1)
conf_data.set('HAVE_SETLOCALE', 1)
conf_data.set('SEPCHAR', '\':\'')
conf_data.set('EMACS_CONFIG_OPTIONS', '""')
conf_data.set('EMACS_CONFIG_FEATURES', '""')
conf_data.set('my_strftime', 'nstrftime')
conf_data.set('TERMINFO', 1)
conf_data.set('USE_NCURSES', 1)
conf_data.set('HAVE_TERM_H', 1)
conf_data.set('GC_SETJMP_WORKS', 1)

conf_data.set('IS_ANY_SEP(_c_)', '(IS_DIRECTORY_SEP(_c_))')
conf_data.set('IS_DEVICE_SEP(_c_)', '0')
conf_data.set('IS_DIRECTORY_SEP(_c_)', '((_c_) == DIRECTORY_SEP)')


conf_data.set('GNU_LINUX', true)


conf_data.set('SYSTEM_TYPE', '"emscripten"')
conf_data.set('EMACS_CONFIGURATION', '"wasm32-emscripten"')

conf_data.set('PACKAGE_BUGREPORT', '"bug-gnu-emacs@gnu.org"')
conf_data.set('PACKAGE_NAME "GNU', 'Emacs"')
conf_data.set('PACKAGE_STRING', '"GNU Emacs 28.0"')
conf_data.set('PACKAGE_TARNAME', '"emacs"')
conf_data.set('PACKAGE_URL', '"http://www.gnu.org/software/emacs/"')
conf_data.set('PACKAGE_VERSION', '"28.0"')

conf_data.set('COPYRIGHT', '"Copyright (C) 2019 Free Software Foundation, Inc."')



#conf_data.set('HAVE_MODULES', 1)

#conf_data.set('TERMINFO', 1)

conf_data.set('_GL_INLINE_HEADER_BEGIN', true)
conf_data.set('_GL_INLINE_HEADER_END', true)
#conf_data.set('INLINE_HEADER_BEGIN', true)
#conf_data.set('INLINE_HEADER_END', true)
#conf_data.set('INLINE', 'static inline')
conf_data.set('_GL_EXTERN_INLINE', 'extern inline')
conf_data.set('_GL_INLINE', 'static inline')

# Not using
#conf_data.set('_GL_INLINE', 'inline')
#conf_data.set('_GL_EXTERN_INLINE', 'extern inline')
#conf_data.set('_GL_EXTERN_INLINE_IN_USE', true)


#define HAVE_LIMITS_H 1
#define HAVE_LINUX_FS_H 1
#define HAVE_LINUX_SYSINFO 1
#define HAVE_LOCALTIME_R 1
#define HAVE_LOG2 1
#define HAVE_LONG_LONG_INT 1
#define HAVE_LRAND48 1
#define HAVE_LSTAT 1
#define HAVE_LUTIMES 1
#define HAVE_MALLOC_H 1
#define HAVE_MBSTATE_T 1
#define HAVE_MEMORY_H 1
#define HAVE_MEMRCHR 1
#define HAVE_MKOSTEMP 1
#define HAVE_MMAP 1
#define HAVE_NET_IF_H 1
#define HAVE_NEWLOCALE 1
#define HAVE_PERSONALITY_ADDR_NO_RANDOMIZE 1
#define HAVE_PIPE2 1

configure_file(output : 'config-def.h',
               configuration : conf_data)
gnu_lib = static_library('gnu', sources, c_args: c_flags, include_directories: inc_dirs)
gnu_dep = declare_dependency(link_with: gnu_lib)
