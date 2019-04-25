function align_roundup()
{
    local src_file=${1}

    filesize=$(stat -c%s "${src_file}")
    if [[ $(( filesize % 4096 )) -ne 0 ]]; then
        echo "Rounding UP ${src_file} to a multiple of 4 KiB."
        : $(( filesize = (filesize + 4095) & -4096 ))
        
        truncate_file "${src_file}" "${filesize}"
    fi
}

function truncate_file() {
  local file_path="$1"
  local file_size="$2"
  echo "truncate and final size = ${filesize}"
  perl -e "open(FILE, \"+<\", \$ARGV[0]); \
           truncate(FILE, ${file_size}); \
           close(FILE);" "${file_path}"
}
