find_package(PkgConfig)

PKG_CHECK_MODULES(PC_GR_TOYTANK gnuradio-toyTank)

FIND_PATH(
    GR_TOYTANK_INCLUDE_DIRS
    NAMES gnuradio/toyTank/api.h
    HINTS $ENV{TOYTANK_DIR}/include
        ${PC_TOYTANK_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    GR_TOYTANK_LIBRARIES
    NAMES gnuradio-toyTank
    HINTS $ENV{TOYTANK_DIR}/lib
        ${PC_TOYTANK_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
          )

include("${CMAKE_CURRENT_LIST_DIR}/gnuradio-toyTankTarget.cmake")

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(GR_TOYTANK DEFAULT_MSG GR_TOYTANK_LIBRARIES GR_TOYTANK_INCLUDE_DIRS)
MARK_AS_ADVANCED(GR_TOYTANK_LIBRARIES GR_TOYTANK_INCLUDE_DIRS)
