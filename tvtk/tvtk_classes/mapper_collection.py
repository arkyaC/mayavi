# Automatically generated code: EDIT AT YOUR OWN RISK
from traits import api as traits
from traitsui import api as traitsui

from tvtk import vtk_module as vtk
from tvtk import tvtk_base
from tvtk.tvtk_base_handler import TVTKBaseHandler
from tvtk import messenger
from tvtk.tvtk_base import deref_vtk
from tvtk import array_handler
from tvtk.array_handler import deref_array
from tvtk.tvtk_classes.tvtk_helper import wrap_vtk

from tvtk.tvtk_classes.collection import Collection


class MapperCollection(Collection):
    """
    MapperCollection - a list of mappers
    
    Superclass: Collection
    
    MapperCollection represents and provides methods to manipulate a
    list of mappers (i.e., Mapper and subclasses). The list is
    unsorted and duplicate entries are not prevented.
    
    See Also:
    
    Mapper Collection
    
    """
    def __init__(self, obj=None, update=True, **traits):
        tvtk_base.TVTKBase.__init__(self, vtk.vtkMapperCollection, obj, update, **traits)
    
    def _get_last_item(self):
        return wrap_vtk(self._vtk_obj.GetLastItem())
    last_item = traits.Property(_get_last_item, help=\
        """
        Get the last mapper in the list.
        """
    )

    def _get_next_item(self):
        return wrap_vtk(self._vtk_obj.GetNextItem())
    next_item = traits.Property(_get_next_item, help=\
        """
        Get the next mapper in the list.
        """
    )

    def _get_next_mapper(self):
        return wrap_vtk(self._vtk_obj.GetNextMapper())
    next_mapper = traits.Property(_get_next_mapper, help=\
        """
        Reentrant safe way to get an object in a collection. Just pass
        the same cookie back and forth.
        """
    )

    _updateable_traits_ = \
    (('reference_count', 'GetReferenceCount'), ('debug', 'GetDebug'),
    ('global_warning_display', 'GetGlobalWarningDisplay'))
    
    _full_traitnames_list_ = \
    (['debug', 'global_warning_display'])
    
    def trait_view(self, name=None, view_element=None):
        if view_element is not None or name not in (None, '', 'traits_view', 'full_traits_view', 'view'):
            return super(MapperCollection, self).trait_view(name, view_element)
        if name == 'full_traits_view':
            full_traits_view = \
            traitsui.View((traitsui.Item("handler._full_traits_list",show_label=False)),
            title='Edit MapperCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return full_traits_view
        elif name == 'view':
            view = \
            traitsui.View(([], [], []),
            title='Edit MapperCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return view
        elif name in (None, 'traits_view'):
            traits_view = \
            traitsui.View((traitsui.HGroup(traitsui.spring, "handler.view_type", show_border=True), 
            traitsui.Item("handler.info.object", editor = traitsui.InstanceEditor(view_name="handler.view"), style = "custom", show_label=False)),
            title='Edit MapperCollection properties', scrollable=True, resizable=True,
            handler=TVTKBaseHandler,
            buttons=['OK', 'Cancel'])
            return traits_view
            
