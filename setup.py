import os
import sys

import tensorflow as tf

includes=tf.sysconfig.get_include()
TF_LIB=tf.sysconfig.get_lib()

# Compile the TensorFlow ops.
compile_command = ("g++ -std=c++11 -shared ./autogp/util/tf_ops/vec_to_tri.cc "
                   "./autogp/util/tf_ops/tri_to_vec.cc -o ./autogp/util/tf_ops/matpackops.so "
                   " -L'"+TF_LIB+"' -ltensorflow_framework "
                   "-fPIC -I '" + includes +"'" )

print compile_command

if sys.platform == "darwin":
    compile_command += " -undefined dynamic_lookup"

if sys.platform == "linux2":
    compile_command += " -D_GLIBCXX_USE_CXX11_ABI=0 "

os.system(compile_command)
