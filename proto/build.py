#!/usr/bin/env python3

from grpc_tools import protoc
import pkg_resources

import os.path
import pathlib

base = pathlib.Path(os.path.relpath(__file__)).parent

args = list(map(str, (
    '-I', base / 'hyperspace-rpc/',
    '-I', base / 'frando-hrpc.proto/',
    '--grpc_python_out', base / '../hyperspace_rpc/',
    '--python_out', base / '../hyperspace_rpc/',
    base / 'hyperspace-rpc/schema.proto',
    base / 'frando-hrpc.proto/hrpc.proto',
)))
proto_include = pkg_resources.resource_filename('grpc_tools', '_proto')

def main():
    protoc.main([''] + args + ['-I{}'.format(proto_include)])

if __name__ == '__main__':
    main()
