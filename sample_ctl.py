#!/usr/bin/env python
import argparse


def add_verbose_to_parser(parser):
    parser.add_argument('--verbose', action='count', default=0)


def add_debug_to_parser(parser):
    parser.add_argument('--debug', action='store_true')


def add_dry_run_to_parser(parser):
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--dry-run', action='store_true', default=True)
    group.add_argument('--force', action='store_false', dest='dry_run')


def parse_arguments(args=None):
    parser = argparse.ArgumentParser(description='argparse demo')

    subparsers = parser.add_subparsers()

    parser_list = subparsers.add_parser('list')
    parser_list.add_argument('--category')
    add_verbose_to_parser(parser_list)
    add_debug_to_parser(parser_list)

    parser_get = subparsers.add_parser('get')
    parser_get.add_argument('--category', required=True)
    parser_get.add_argument('--key', required=True)
    add_verbose_to_parser(parser_get)
    add_debug_to_parser(parser_get)

    parser_upsert = subparsers.add_parser('upsert')
    parser_upsert.add_argument('--category', required=True)
    parser_upsert.add_argument('--key', required=True)
    add_dry_run_to_parser(parser_upsert)
    add_verbose_to_parser(parser_upsert)
    add_debug_to_parser(parser_upsert)

    parser_delete = subparsers.add_parser('delete')
    parser_delete.add_argument('--category', required=True)
    parser_delete.add_argument('--key', required=True)
    add_dry_run_to_parser(parser_delete)
    add_verbose_to_parser(parser_delete)
    add_debug_to_parser(parser_delete)

    return parser.parse_args(args)


if __name__ == '__main__':
    args = parse_arguments()
    print(args)
