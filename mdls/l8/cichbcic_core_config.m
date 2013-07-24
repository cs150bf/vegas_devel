
function cichbcic_core_config(this_block)

  % Revision History:
  %
  %   20-Mar-2013  (23:40 hours):
  %     Original code was machine generated by Xilinx's System Generator after parsing
  %     /tools/casper/projects/hong/my_vegas_devel/mode13/cichbcic_core.vhd
  %
  %

  this_block.setTopLevelLanguage('VHDL');

  this_block.setEntityName('cichbcic_core');

  % System Generator has to assume that your entity  has a combinational feed through; 
  %   if it  doesn't, then comment out the following line:
  %this_block.tagAsCombinational;

  this_block.addSimulinkInport('in0');
  this_block.addSimulinkInport('in1');
  this_block.addSimulinkInport('in2');
  this_block.addSimulinkInport('in3');
  this_block.addSimulinkInport('in4');
  this_block.addSimulinkInport('in5');
  this_block.addSimulinkInport('in6');
  this_block.addSimulinkInport('in7');
  this_block.addSimulinkInport('in8');
  this_block.addSimulinkInport('in9');
  this_block.addSimulinkInport('in10');
  this_block.addSimulinkInport('in11');
  this_block.addSimulinkInport('in12');
  this_block.addSimulinkInport('in13');
  this_block.addSimulinkInport('in14');
  this_block.addSimulinkInport('in15');
  this_block.addSimulinkInport('sync_in');

  this_block.addSimulinkOutport('out_x0');

  out_x0_port = this_block.port('out_x0');
  out_x0_port.setType('Fix_32_6');

  % -----------------------------
  if (this_block.inputTypesKnown)
    % do input type checking, dynamic output type and generic setup in this code block.

    if (this_block.port('in0').width ~= 24);
      this_block.setError('Input data type for port "in0" must have width=24.');
    end

    if (this_block.port('in1').width ~= 24);
      this_block.setError('Input data type for port "in1" must have width=24.');
    end

    if (this_block.port('in10').width ~= 24);
      this_block.setError('Input data type for port "in10" must have width=24.');
    end

    if (this_block.port('in11').width ~= 24);
      this_block.setError('Input data type for port "in11" must have width=24.');
    end

    if (this_block.port('in12').width ~= 24);
      this_block.setError('Input data type for port "in12" must have width=24.');
    end

    if (this_block.port('in13').width ~= 24);
      this_block.setError('Input data type for port "in13" must have width=24.');
    end

    if (this_block.port('in14').width ~= 24);
      this_block.setError('Input data type for port "in14" must have width=24.');
    end

    if (this_block.port('in15').width ~= 24);
      this_block.setError('Input data type for port "in15" must have width=24.');
    end

    if (this_block.port('in2').width ~= 24);
      this_block.setError('Input data type for port "in2" must have width=24.');
    end

    if (this_block.port('in3').width ~= 24);
      this_block.setError('Input data type for port "in3" must have width=24.');
    end

    if (this_block.port('in4').width ~= 24);
      this_block.setError('Input data type for port "in4" must have width=24.');
    end

    if (this_block.port('in5').width ~= 24);
      this_block.setError('Input data type for port "in5" must have width=24.');
    end

    if (this_block.port('in6').width ~= 24);
      this_block.setError('Input data type for port "in6" must have width=24.');
    end

    if (this_block.port('in7').width ~= 24);
      this_block.setError('Input data type for port "in7" must have width=24.');
    end

    if (this_block.port('in8').width ~= 24);
      this_block.setError('Input data type for port "in8" must have width=24.');
    end

    if (this_block.port('in9').width ~= 24);
      this_block.setError('Input data type for port "in9" must have width=24.');
    end

    if (this_block.port('sync_in').width ~= 1);
      this_block.setError('Input data type for port "sync_in" must have width=1.');
    end

    this_block.port('sync_in').useHDLVector(false);

  end  % if(inputTypesKnown)
  % -----------------------------

  % -----------------------------
   if (this_block.inputRatesKnown)
     setup_as_single_rate(this_block,'clk_1','ce_1')
   end  % if(inputRatesKnown)
  % -----------------------------

    % (!) Set the inout port rate to be the same as the first input 
    %     rate. Change the following code if this is untrue.
    uniqueInputRates = unique(this_block.getInputRates);


  % Add addtional source files as needed.
  %  |-------------
  %  | Add files in the order in which they should be compiled.
  %  | If two files "a.vhd" and "b.vhd" contain the entities
  %  | entity_a and entity_b, and entity_a contains a
  %  | component of type entity_b, the correct sequence of
  %  | addFile() calls would be:
  %  |    this_block.addFile('b.vhd');
  %  |    this_block.addFile('a.vhd');
  %  |-------------

  %    this_block.addFile('');
  %    this_block.addFile('');
  this_block.addFile('cichbcic_core.vhd');

return;


% ------------------------------------------------------------

function setup_as_single_rate(block,clkname,cename) 
  inputRates = block.inputRates; 
  uniqueInputRates = unique(inputRates); 
  if (length(uniqueInputRates)==1 & uniqueInputRates(1)==Inf) 
    block.addError('The inputs to this block cannot all be constant.'); 
    return; 
  end 
  if (uniqueInputRates(end) == Inf) 
     hasConstantInput = true; 
     uniqueInputRates = uniqueInputRates(1:end-1); 
  end 
  if (length(uniqueInputRates) ~= 1) 
    block.addError('The inputs to this block must run at a single rate.'); 
    return; 
  end 
  theInputRate = uniqueInputRates(1); 
  for i = 1:block.numSimulinkOutports 
     block.outport(i).setRate(theInputRate); 
  end 
  block.addClkCEPair(clkname,cename,theInputRate); 
  return; 

% ------------------------------------------------------------
