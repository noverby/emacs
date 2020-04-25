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

link_flags = ['-o', 'hello.html', '-Llib', '-lgnu', '-Lsubprojects/ncurses', '-lncurses']
exe = executable('emacs', sources, c_args: c_flags, link_args: link_flags,
                 dependencies: [
                   # ncurses_dep, gnu_dep, m_dep, thread_dep, dl_dep, rt_dep,
                   z_dep,
                 ],
                 include_directories: inc_dirs)
